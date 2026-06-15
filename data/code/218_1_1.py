def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for x in data[1:]:
        if x < minimum:
            minimum = x
    return minimum
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_minimum(sample_list)
    print(result)