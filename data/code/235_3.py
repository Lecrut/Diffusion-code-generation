def print_square(rows):
    for i in range(rows):
        for j in range(rows):
            print('*', end='')
        print()
if __name__ == '__main__':
    print("--- 3x3 Square ---")
    print_square(3)
    print("\n--- 5x5 Square ---")
    print_square(5)