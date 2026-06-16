def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    current_maximum = data[0]
    for element in data[1:]:
        if element > current_maximum:
            current_maximum = element
    return current_maximum
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    maximum_element = find_maximum(sample_list)
    print(maximum_element)