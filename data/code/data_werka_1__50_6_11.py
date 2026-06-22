def non_negative_difference(a, b):
    try:
        return abs(a - b)
    except TypeError as e:
        raise ValueError("Both inputs must be numbers") from e

if __name__ == '__main__':
    sample_values = [(10, 5), (3, 7), (-2, -8), (0, 0)]
    for a, b in sample_values:
        print(non_negative_difference(a, b))