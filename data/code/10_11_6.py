def get_first_item(arr):
    if len(arr) == 0:
        return None
    return arr[0]

if __name__ == '__main__':
    sample_data_empty = []
    sample_data_filled = [42, 99, 17]
    print(get_first_item(sample_data_empty))
    print(get_first_item(sample_data_filled))