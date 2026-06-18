def multiply_grid(rows, cols):
    result = []
    for i in range(rows):
        row_result = []
        for j in range(cols):
            product = 0
            for k in range(cols):
                product += (i + 1) * (j + 1) * (k + 1)
            row_result.append(product)
        result.append(row_result)
    return result
if __name__ == '__main__':
    grid_size = 3
    multiplication_results = multiply_grid(grid_size, grid_size)
    for row in multiplication_results:
        print(row)