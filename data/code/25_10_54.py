ZERO_THRESHOLD = 1e-9

def is_zero(x):
    return abs(x) < ZERO_THRESHOLD if isinstance(x, (int, float)) else False

if __name__ == '__main__':
    sample_values = [0, 1, -1, 2.5, None, '', [], {}, 1e-10, -1e-10]
    results = {x: is_zero(x) for x in sample_values}
    print(results)