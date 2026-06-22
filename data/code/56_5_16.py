def validate_grid_size(size):
    if not isinstance(size, int):
        raise TypeError("Grid size must be an integer")
    if size < 1:
        raise ValueError("Grid size must be positive")
    return size

def generate_multiplication_grid():
    size = validate_grid_size(10)
    return [[i * j for j in range(1, size + 1)] for i in range(1, size + 1)]

if __name__ == '__main__':
    try:
        result_grid = generate_multiplication_grid()
        for row in result_grid:
            print('\t'.join(map(str, row)))
    except (TypeError, ValueError) as e:
        print(e)