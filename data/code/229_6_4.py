def generate_sum_grid(size):
    grid = [[i + j for j in range(size)] for i in range(size)]
    return grid

if __name__ == '__main__':
    sample_grid = generate_sum_grid(20)
    for row in sample_grid:
        print(row)