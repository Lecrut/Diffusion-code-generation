def get_middle_item(array):
    middle_index = len(array) // 2
    return array[middle_index]
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    middle_item = get_middle_item(sample_data)
    print(middle_item)