def get_middle_value(lst):
    if not lst:
        raise ValueError('Cannot get middle value of an empty list')
    middle_index = len(lst) // 2
    return lst[middle_index]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    middle_value = get_middle_value(sample_list)
    print(middle_value)