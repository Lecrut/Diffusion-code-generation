import numpy as np
def is_even_mathematical(x):
    return x % 2 == 0
if __name__ == '__main__':
    sample_values = [1, 2, -3, 4.5, 6]
    results = []
    for val in sample_values:
        try:
            evenness = is_even_mathematical(val)
            results.append((val, bool(evenness)))
        except TypeError:
            results.append((val, False))
    print(results)