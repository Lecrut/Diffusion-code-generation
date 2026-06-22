def generate_multiplication_grid():
    return [[row * col for col in range(1, 11)] for row in range(1, 11)]

if __name__ == '__main__':
    grid = generate_multiplication_grid()
    for row in grid:
        print(row)