def find_middle_element(input_list):
    if not input_list:
        raise ValueError("List must not be empty")
    length = len(input_list)
    start = (length - 1) // 2
    end = start + 1
    middle_slice = input_list[start:end]
    return middle_slice[0]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 60, 70]
    value = find_middle_element(sample_data)
    print(value)