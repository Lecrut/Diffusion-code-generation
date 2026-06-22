def get_middle_item(array):
    return array[len(array) // 2]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_middle_item(sample_data)
    print(result)
    sample_data_even = [1, 2, 3, 4]
    result_even = get_middle_item(sample_data_even)
    print(result_even)