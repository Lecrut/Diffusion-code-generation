def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
            if (j + 1) % size == 0:
                print()
if __name__ == '__main__':
    print_square(5)