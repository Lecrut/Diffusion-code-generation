def print_square_grid(size):
    for i in range(size):
        row = ""
        for j in range(size):
            if i == 0:
                row += "#"
            elif j == 0:
                row += "#"
            else:
                row += " "
        print(row)
if __name__ == '__main__':
    print("--- 3x3 Grid ---")
    print_square_grid(3)
    print("\n--- 5x5 Grid ---")
    print_square_grid(5)