def print_grid():
    size = 5
    for i in range(size):
        for j in range(size):
            print("*", end="")
        print()
if __name__ == '__main__':
    print_grid()