from collections import defaultdict


def build_cache(cache, m, n, board):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cache[board[i][j]].append((i, j))


def get_next_cells(row1, col1, cache):
    return cache[row1 * col1]


def solve(sol, row, col, m, n, cache):
    stack = []
    stack.append((row, col))
    sol[row][col] = 1
    while stack:
        r, c = stack.pop()
        if r == 1 and c == 1:
            return True
        for r1, c1 in get_next_cells(r, c, cache):
            if sol[r1][c1] == 0:
                stack.append((r1, c1))
                sol[r1][c1] = 1
    return False


m = int(input())
n = int(input())

sol = [[0 for i in range(n + 1)] for j in range(m + 1)]
board = list()
board.append([0 for i in range(n + 1)])

for i in range(m):
    l = [0]
    l.extend([int(x) for x in input().split()])
    board.append(l)

cell_cache = defaultdict(list)

build_cache(cell_cache, m, n, board)

if solve(sol, m, n, m, n, cell_cache):
    print("yes")
else:
    print("no")