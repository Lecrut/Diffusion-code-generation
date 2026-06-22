def get_middle_item(array):
    return array[len(array) // 2]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(get_middle_item(sample_data))
    sample_data_even = [10, 20, 30, 40]
    print(get_middle_item(sample_data_even))