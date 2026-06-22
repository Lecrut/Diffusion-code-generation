def get_penultimate_element(input_list):
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    if len(input_list) < 2:
        raise ValueError("List must contain at least two elements")
    return input_list[-2]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(get_penultimate_element(sample_data))