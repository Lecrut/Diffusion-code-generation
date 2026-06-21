def get_middle_item(array):
    if not array:
        return None
    return array[len(array) // 2]

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    print(get_middle_item(sample_data))
    sample_data_even = [1, 2, 3, 4]
    print(get_middle_item(sample_data_even))
    sample_data_single = [42]
    print(get_middle_item(sample_data_single))
    sample_data_empty = []
    print(get_middle_item(sample_data_empty))