def print_grid():
    width = 10
    height = 5
    for y in range(height):
        for x in range(width):
            print("#", end="")
        print()
if __name__ == '__main__':
    print_grid()