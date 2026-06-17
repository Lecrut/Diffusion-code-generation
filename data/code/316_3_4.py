def print_hollow_square(R):
    for i in range(R):
        for j in range(R):
            if i == 0 or i == R - 1 or j == 0 or j == R - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
if __name__ == '__main__':
    R1 = 5
    print("Hollow square of size", R1, "x", R1)
    print_hollow_square(R1)
    R2 = 8
    print("\nHollow square of size", R2, "x", R2)
    print_hollow_square(R2)