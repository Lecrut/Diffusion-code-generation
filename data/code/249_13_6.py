def find_largest_element(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for element in data[1:]:
        if element > largest:
            largest = element
    return largest

if __name__ == '__main__':
    sample_list = [15, 8, 42, 3, 99, 27]
    result = find_largest_element(sample_list)
    print(result)