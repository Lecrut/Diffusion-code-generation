def get_center_element(data):
    if not data:
        raise ValueError("Sequence cannot be empty")
    center_index = len(data) // 2
    return data[center_index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = (1, 2, 3, 4, 5, 6, 7)
    print(get_center_element(sample_list))
    print(get_center_element(sample_tuple))