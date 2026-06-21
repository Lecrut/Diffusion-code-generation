def find_middle_element(data):
    if not data:
        raise ValueError("Input sequence cannot be empty")
    middle_index = len(data) // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    result = find_middle_element(sample_tuple)
    print(result)