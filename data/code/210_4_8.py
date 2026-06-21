def find_range(data):
    if not data:
        raise ValueError("Data list cannot be empty")
    minimum = min(data)
    maximum = max(data)
    return (minimum, maximum)

if __name__ == '__main__':
    sample_values = [
        [1, 5, 2, 8, 3],
        [],
        [10],
        [-5, 0, 5]
    ]
    
    for values in sample_values:
        try:
            print(f"Range of {values}: {find_range(values)}")
        except ValueError as e:
            print(e)