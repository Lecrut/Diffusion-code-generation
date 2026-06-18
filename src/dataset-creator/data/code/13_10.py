def multiply_grid(rows, cols):
    result = []
    for i in range(rows):
        row_data = []
        for j in range(cols):
            product = 0
            for k in range(cols):
                product += (i + 1) * (j + 1)
            row_data.append([product])
        result.append(row_data)
    return result
if __name__ == '__main__':
    grid_size = 3
    multiplication_table = multiply_grid(grid_size, grid_size)
    for row in multiplication_table:
        print(row)