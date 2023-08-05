# find_next_empty searches for the next empty cell
# which I will represent with a value of minus one (-1).
def find_next_empty(problem):
    for r in range(9):
        for c in range(9):
            if problem[r][c] == -1:
                return r, c

    return None, None


# is_valid checks whether the guess is valid for
# that given cell or not. Returns true if valid, and
# returns false if not
def is_valid(problem, guess, row, col):
    # Checking whether the guess exists in the row
    row_vals = problem[row]
    if guess in row_vals:
        return False

    # Checking whether the guess exists in the column
    # Could have been replaced with
    # col_vals = [problem[i][col] for i in range(9)]
    col_vals = []
    for i in range(9):
        col_vals.append(problem[i][col])
    if guess in col_vals:
        return False

    # Checking whether the guess exists in the
    # same square as the cell
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if guess == problem[r][c]:
                return False

    # If code reaches this part, then the guess is valid
    # as the guess does not exist on the same row, column
    # or box, so we can return True
    return True


# solve_sudoku will recursively try to solve the given
# problem using a backtrack method
def solve_sudoku(problem):
    row, col = find_next_empty(problem)

    if row is None:
        return True

    for guess in range(1, 10):
        if is_valid(problem, guess, row, col):
            problem[row][col] = guess
            if solve_sudoku(problem):
                return True
        problem[row][col] = -1

    return False


s =\
        [
            [ 3, -1, -1,  -1,  5, -1,   -1, -1, -1],
            [-1, -1, -1,   2, -1, -1,    9, -1,  5],
            [-1, -1, -1,   7,  1,  9,   -1,  8, -1],

            [-1,  5, -1,   -1,  6,  8,   -1, -1, -1],
            [ 2, -1,  6,   -1, -1,  3,   -1, -1, -1],
            [-1, -1, -1,   -1, -1, -1,   -1, -1,  4],

            [ 5, -1, -1,   -1, -1, -1,   -1, -1, -1],
            [ 6,  7, -1,    1, -1,  5,   -1,  4, -1],
            [ 1, -1,  9,   -1, -1, -1,    2, -1, -1]
        ]

if solve_sudoku(s):
    print("_ _ _ _ _ _ _ _ _ _ _ _ _")
    print(f"| {s[0][0]} {s[0][1]} {s[0][2]} | {s[0][3]} {s[0][4]} {s[0][5]} | {s[0][6]} {s[0][7]} {s[0][8]} |")
    print(f"| {s[1][0]} {s[1][1]} {s[1][2]} | {s[1][3]} {s[1][4]} {s[1][5]} | {s[1][6]} {s[1][7]} {s[1][8]} |")
    print(f"| {s[2][0]} {s[2][1]} {s[2][2]} | {s[2][3]} {s[2][4]} {s[2][5]} | {s[2][6]} {s[2][7]} {s[2][8]} |")
    print("| _ _ _ | _ _ _ | _ _ _ |")
    print(f"| {s[3][0]} {s[3][1]} {s[3][2]} | {s[3][3]} {s[3][4]} {s[3][5]} | {s[3][6]} {s[3][7]} {s[3][8]} |")
    print(f"| {s[4][0]} {s[4][1]} {s[4][2]} | {s[4][3]} {s[4][4]} {s[4][5]} | {s[4][6]} {s[4][7]} {s[4][8]} |")
    print(f"| {s[5][0]} {s[5][1]} {s[5][2]} | {s[5][3]} {s[5][4]} {s[5][5]} | {s[5][6]} {s[5][7]} {s[5][8]} |")
    print("| _ _ _ | _ _ _ | _ _ _ |")
    print(f"| {s[6][0]} {s[6][1]} {s[6][2]} | {s[6][3]} {s[6][4]} {s[6][5]} | {s[6][6]} {s[6][7]} {s[6][8]} |")
    print(f"| {s[7][0]} {s[7][1]} {s[7][2]} | {s[7][3]} {s[7][4]} {s[7][5]} | {s[7][6]} {s[7][7]} {s[7][8]} |")
    print(f"| {s[8][0]} {s[8][1]} {s[8][2]} | {s[8][3]} {s[8][4]} {s[8][5]} | {s[8][6]} {s[8][7]} {s[8][8]} |")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _")
else:
    print("No Solution Exists!")
