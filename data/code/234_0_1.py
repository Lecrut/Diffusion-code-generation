if __name__ == '__main__':
    size = 5
    for i in range(size):
        for j in range(size):
            if (i + j) % 2 == 0:
                print(" " * j + "#", end="")
            else:
                print("  ", end="")
        print()