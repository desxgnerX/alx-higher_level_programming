#!/usr/bin/python3
# 101-nqueens.py
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""import sys
''' 
    column first element, row second element
'''
def reject(board):
    for col_A in board:
        for col_B in board:
            if not col_A is col_B:
                if col_A[0] == col_B[0]:
                    return True
                if col_A[1] == col_B[1]:
                    return True
                if col_A[1] - col_A[0] == col_B[1] - col_B[0]:
                    return True
                if col_A[0] + col_A[1] == col_B[0] + col_B[1]:
                    return True
    return False
