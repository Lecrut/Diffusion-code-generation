def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    maximum = data[0]
    for element in data[1:]:
        if element > maximum:
            maximum = element
    return maximum
if __name__ == '__main__':
    sample_list = [3, 1, 9, 4, 7, 2]
    max_element = find_maximum(sample_list)
    print(max_element)