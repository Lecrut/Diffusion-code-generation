ZERO = 0

def is_zero(value):
    return value == ZERO

if __name__ == '__main__':
    test_values = [0, 1, -2, 3.14, 0j]
    results = {val: is_zero(val) for val in test_values}
    print(results)