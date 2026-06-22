def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for number in data[1:]:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample_list = [34.5, 12.7, 56.8, 9.2, 88.1, 23.0, 7.6]
    result = find_minimum(sample_list)
    print(result)