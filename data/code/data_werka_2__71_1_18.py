def find_middle_element(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list")
    length = len(data)
    if length == 0:
        raise ValueError("List cannot be empty")
    lower_mid_index = (length - 1) // 2
    return data[lower_mid_index]

if __name__ == '__main__':
    sample_odd = [7, 8, 9, 10, 11]
    sample_even = [2, 4, 6, 8]
    sample_single = [42]
    print(find_middle_element(sample_odd))
    print(find_middle_element(sample_even))
    print(find_middle_element(sample_single))