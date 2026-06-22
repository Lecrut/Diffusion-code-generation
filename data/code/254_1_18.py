def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for value in data[1:]:
        if value < minimum:
            minimum = value
    return minimum

if __name__ == '__main__':
    sample_list = [34.5, 12.3, 56.7, 9.8, 88.9, 23.4, 7.0]
    result = find_minimum(sample_list)
    print(result)