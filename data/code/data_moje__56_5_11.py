def _scale_value(val, factor):
    return val * factor

def generate_multiplication_grid():
    multiplier_map = {
        'base': 1,
        'shift': 0
    }
    start = multiplier_map['base'] + multiplier_map['shift']
    end = start + 10
    return [[_scale_value(r, c) for c in range(start, end)] for r in range(start, end)]

if __name__ == '__main__':
    result = generate_multiplication_grid()
    for line in result:
        print(line)