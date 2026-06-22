def print_hollow_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(1, rows - i + 1):
            print(" ", end="")
        for j in range(1, 2 * i):
            if i == 1 or i == rows or j == 1 or j == 2 * i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

if __name__ == '__main__':
    print_hollow_pyramid(5)