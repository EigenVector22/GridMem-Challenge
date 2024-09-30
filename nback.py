import random
import os
import msvcrt

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_grid(n, m):
    numbers = list(range(1, m + 1))
    grid = [[0 for _ in range(n)] for _ in range(n)]
    positions = random.sample(range(n * n), m)
    
    for i, pos in enumerate(positions):
        row, col = divmod(pos, n)
        grid[row][col] = numbers[i]
    
    return grid

def display_grid(grid, cursor_row, cursor_col):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if i == cursor_row and j == cursor_col:
                print(f"[{grid[i][j]:2}]", end="")
            else:
                print(f" {grid[i][j]:2} ", end="")
        print()

def get_key():
    key = msvcrt.getch()
    if key == b'\xe0':  # Arrow key prefix
        key = msvcrt.getch()
        return {
            b'H': 'up',
            b'P': 'down',
            b'K': 'left',
            b'M': 'right'
        }.get(key, None)
    return key.decode('utf-8').lower()

def play_game(n, m, rounds):
    for round in range(1, rounds + 1):
        grid = create_grid(n, m)
        
        clear_screen()
        print(f"Round {round}/{rounds}")
        print("Memorize the grid and press Enter when ready.")
        display_grid(grid, -1, -1)
        input()

        empty_grid = [[0 for _ in range(n)] for _ in range(n)]
        current_number = 1
        cursor_row, cursor_col = 0, 0

        while current_number <= m:
            clear_screen()
            print(f"Round {round}/{rounds}")
            print(f"Select position for number {current_number}")
            print("Use arrow keys to move, Space to select")
            display_grid(empty_grid, cursor_row, cursor_col)

            key = get_key()
            if key == 'up' and cursor_row > 0:
                cursor_row -= 1
            elif key == 'down' and cursor_row < n - 1:
                cursor_row += 1
            elif key == 'left' and cursor_col > 0:
                cursor_col -= 1
            elif key == 'right' and cursor_col < n - 1:
                cursor_col += 1
            elif key == ' ':
                if grid[cursor_row][cursor_col] == current_number:
                    empty_grid[cursor_row][cursor_col] = current_number
                    current_number += 1
                else:
                    print("Incorrect! Game over.")
                    input("Press Enter to continue...")
                    return

        print("Correct! Round complete.")
        input("Press Enter to continue...")

    print("Congratulations! You've completed all rounds.")

def main():
    n = int(input("Enter the size of the grid (n for n x n): "))
    m = int(input(f"Enter the number of items to remember (1-{n*n}): "))
    rounds = int(input("Enter the number of rounds: "))

    if m > n * n:
        print(f"Error: m cannot be greater than {n*n}")
        return

    play_game(n, m, rounds)

if __name__ == "__main__":
    main()