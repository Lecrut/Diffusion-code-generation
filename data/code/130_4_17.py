ZERO = 0

def is_zero(value):
    return value == ZERO

if __name__ == '__main__':
    sample_values = [0, 1, -2, 3.14, 0j]
    for val in sample_values:
        print(is_zero(val))