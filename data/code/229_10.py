def generate_square_grid(size):
    for i in range(size):
        row = ""
        for j in range(size):
            row += "* "
        print(row)
if __name__ == '__main__':
    grid_size = 5
    generate_square_grid(grid_size)