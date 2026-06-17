def print_grid():
    rows = 5
    cols = 5
    for i in range(rows):
        for j in range(cols):
            print("*", end="")
        print()
if __name__ == '__main__':
    print_grid()