def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return min(data)

if __name__ == '__main__':
    sample_values = [
        [3, 1, 4, 1, 5, 9, 2],
        [-10, 5, 0, -20, 100],
        [7],
        []
    ]
    for values in sample_values:
        try:
            print(f"Minimum of {values}: {find_minimum(values)}")
        except ValueError as e:
            print(e)