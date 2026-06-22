OPERATORS = {'multiply': lambda x, y: x * y}

def create_grid(operation_map, start, end):
    op = operation_map['multiply']
    return [[op(r, c) for c in range(start, end + 1)] for r in range(start, end + 1)]

def generate_multiplication_grid():
    return create_grid(OPERATORS, 1, 10)

if __name__ == '__main__':
    result = generate_multiplication_grid()
    for line in result:
        print(' '.join(map(str, line)))