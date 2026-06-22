def get_middle_element(data):
    if not data:
        return None
    mid_index = len(data) // 2
    if len(data) % 2 == 1:
        return data[mid_index]
    else:
        return data[mid_index - 1]

if __name__ == '__main__':
    sample_odd = [1, 2, 3, 4, 5]
    sample_even = [10, 20, 30, 40]
    empty_list = []
    print(get_middle_element(sample_odd))
    print(get_middle_element(sample_even))
    print(get_middle_element(empty_list))