def print_star_rectangle(rows, cols):
    for i in range(rows):
        for j in range(cols):
            print("*", end="")
            if (j + 1) % cols == 0:
                print()
if __name__ == '__main__':
    rows = 5
    cols = 10
    print_star_rectangle(rows, cols)