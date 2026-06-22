def generate_multiplication_grid():
    return [[i * j for j in range(1, 11)] for i in range(1, 11)]

if __name__ == '__main__':
    grid = generate_multiplication_grid()
    for row in grid:
        print(row)