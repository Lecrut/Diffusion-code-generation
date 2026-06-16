def print_square(size):
    if not isinstance(size, int) or size <= 0:
        return
    for i in range(size):
        for j in range(size):
            print("#", end="")
            if j < size - 1:
                print(" ", end="")
        print()
if __name__ == '__main__':
    print_square(5)
    print_square(3)
    print_square(1)
    print_square(0)
    print_square(-2)