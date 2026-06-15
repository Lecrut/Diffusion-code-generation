def print_square_grid(size):
    output = ""
    for i in range(size):
        row = ""
        for j in range(size):
            if i == j:
                row += "# "
            else:
                row += ". "
        output += row + "\n"
    print(output)
if __name__ == '__main__':
    print_square_grid(5)