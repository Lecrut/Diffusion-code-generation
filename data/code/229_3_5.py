def print_square(size):
    for i in range(size):
        row = ""
        for j in range(size):
            row += "*"
        print(row)

if __name__ == '__main__':
    square_size = 8
    print_square(square_size)