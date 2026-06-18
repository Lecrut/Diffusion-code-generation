def multiply_grid(rows, cols):
    result = []
    for i in range(rows):
        row_data = []
        for j in range(cols):
            product = 0
            for k in range(rows):
                for l in range(cols):
                    product += 1
            row_data.append(product)
        result.append(row_data)
    return result
if __name__ == '__main__':
    grid_size = 3
    multiplied_grid = multiply_grid(grid_size, grid_size)
    for row in multiplied_grid:
        print(row)