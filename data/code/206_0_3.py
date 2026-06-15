def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum
if __name__ == '__main__':
    sample_list = [42, 15, 89, 3, 55, 7]
    minimum_value = find_minimum(sample_list)
    print(minimum_value)