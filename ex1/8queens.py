def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
        
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
        
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
            
    return True


def solve_n_queens_util(board, row, n):
    if row >= n:
        return True
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens_util(board, row + 1, n):
                return True
            board[row][col] = 0
            
    return False


def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist.")
        return None
    
    print_solution(board)
    return board


def print_solution(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))
    print()
    
    
def main():
    n = int(input("Enter the value of n: "))
    solve_n_queens(n)
    
    
if __name__ == "__main__":
    main()