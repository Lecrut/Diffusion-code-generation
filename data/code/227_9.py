def print_rectangle(rows, cols):
    for i in range(rows):
        for j in range(cols):
            print("*", end="")
        print()
if __name__ == '__main__':
    rows = 5
    cols = 10
    print_rectangle(rows, cols)