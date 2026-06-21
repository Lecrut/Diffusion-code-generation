def find_middle_element(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    length = len(data)
    if length == 0:
        raise ValueError("List must not be empty")
    is_odd = length % 2 != 0
    start_index = (length - 1) // 2
    end_index = (length + 1) // 2
    middle_slice = data[start_index:end_index]
    if is_odd:
        return middle_slice[0]
    return (middle_slice[0] + middle_slice[1]) / 2

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = find_middle_element(sample_data)
    print(result)
    
    sample_even = [10, 20, 30, 40]
    result_even = find_middle_element(sample_even)
    print(result_even)