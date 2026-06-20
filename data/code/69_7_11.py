def get_sublist(original_list, start_index, end_index):
    if not (0 <= start_index <= len(original_list) - 1 and 0 <= end_index <= len(original_list) - 1):
        raise IndexError('Start and end indices must be within the list bounds')
    return original_list[start_index:end_index + 1]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_sublist(sample_list, 1, 3))