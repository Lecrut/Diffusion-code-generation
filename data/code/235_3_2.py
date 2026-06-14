def print_square(rows):
    for i in range(rows):
        for j in range(rows):
            print("*", end="")
            if j < rows - 1:
                print(" ", end="")
        print()
if __name__ == '__main__':
    print("--- Test Case 1 (rows=4) ---")
    print_square(4)
    print("\n--- Test Case 2 (rows=3) ---")
    print_square(3)
    print("\n--- Test Case 3 (rows=1) ---")
    print_square(1)