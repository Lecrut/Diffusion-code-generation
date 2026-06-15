def print_square(rows):
    for i in range(rows):
        for j in range(rows):
            print("*", end="")
            if j < rows - 1:
                print(" ", end="")
        print()
if __name__ == '__main__':
    print_square(5)