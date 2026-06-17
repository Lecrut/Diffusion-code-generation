def print_hollow_square(R):
    for i in range(R):
        for j in range(R):
            if i == 0 or i == R - 1 or j == 0 or j == R - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
if __name__ == '__main__':
    R_sample = 5
    print_hollow_square(R_sample)
    R_sample = 3
    print_hollow_square(R_sample)