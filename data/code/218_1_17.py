def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for value in data[1:]:
        if value < minimum:
            minimum = value
    return minimum

if __name__ == '__main__':
    sample_data = [7, 8, 9, 5, 3, 2, 4, 6, 1, 0]
    result = find_minimum(sample_data)
    print(result)