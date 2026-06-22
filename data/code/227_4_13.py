def print_hollow_square(size):
    if size <= 0:
        return
    for i in range(size):
        line = ""
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                line += "*"
            else:
                line += " "
        print(line)

if __name__ == '__main__':
    square_size = 4
    print_hollow_square(square_size)