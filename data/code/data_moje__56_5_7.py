MAPPING = {
    'min_val': 1,
    'max_val': 10
}

def generate_multiplication_grid():
    start = MAPPING['min_val']
    end = MAPPING['max_val'] + 1
    grid = [
        [x * y for y in range(start, end)]
        for x in range(start, end)
    ]
    return grid

if __name__ == '__main__':
    result = generate_multiplication_grid()
    for row in result:
        print(row)