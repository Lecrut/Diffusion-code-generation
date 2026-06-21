def find_minimum(data):
    if not isinstance(data, list) or not all(isinstance(x, int) for x in data):
        raise ValueError("Input must be a non-empty list of integers")
    if not data:
        raise ValueError("List cannot be empty")
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum

if __name__ == '__main__':
    input_list = [45, 12, 89, 3, 56, 7]
    result = find_minimum(input_list)
    print(result)