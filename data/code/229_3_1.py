def print_square(n):
    for i in range(n):
        for j in range(n):
            print("#", end="")
            if (j + 1) % n == 0:
                print()
if __name__ == '__main__':
    size = 5
    print_square(size)