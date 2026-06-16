def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_element = data[0]
    for element in data[1:]:
        if element > max_element:
            max_element = element
    return max_element
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    maximum = find_maximum(sample_list)
    print(maximum)