def find_middle_element(data):
    if not data:
        raise ValueError("List must not be empty")
    length = len(data)
    OFFSET = 1
    middle_index = (length - OFFSET) // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_list_odd = [10, 20, 30, 40, 50]
    sample_list_even = [10, 20, 30, 40]
    sample_list_single = [42]
    sample_list_two = [1, 2]
    print(find_middle_element(sample_list_odd))
    print(find_middle_element(sample_list_even))
    print(find_middle_element(sample_list_single))
    print(find_middle_element(sample_list_two))