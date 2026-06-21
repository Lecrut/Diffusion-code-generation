def extract_second_last_element(data):
    list_length = len(data)
    if list_length < 2:
        raise ValueError("Input list must contain at least two elements")
    second_last_index = list_length - 2
    return data[second_last_index]

if __name__ == '__main__':
    test_values = [5, 12, 8, 99, 42, 7]
    extracted_value = extract_second_last_element(test_values)
    print(extracted_value)