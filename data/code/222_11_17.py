def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum

if __name__ == '__main__':
    sample_values = [5, 2, 8, 1, 9], [-10, 0, 50, -3], [42]
    for values in sample_values:
        print(f"Minimum of {values}: {find_minimum(values)}")