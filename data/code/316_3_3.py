def print_hollow_square(R):
    for i in range(R):
        for j in range(R):
            if i == 0 or i == R - 1 or j == 0 or j == R - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
if __name__ == '__main__':
    print("--- Square of size 5 ---")
    print_hollow_square(5)
    print("\n--- Square of size 3 ---")
    print_hollow_square(3)