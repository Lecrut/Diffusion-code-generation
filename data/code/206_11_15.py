def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for item in data[1:]:
        if not isinstance(item, int):
            raise TypeError("All elements must be integers")
        if item < minimum:
            minimum = item
    return minimum

if __name__ == '__main__':
    input_list = [45, 12, 89, 3, 56, 7]
    result = find_minimum(input_list)
    print(result)