def get_middle_item(array):
    if not array:
        return None
    index = len(array) // 2
    return array[index]

if __name__ == '__main__':
    primary_set = [3, 7, 1, 9, 2]
    secondary_set = [5, 12, 8, 20]
    single_set = [99]
    print(get_middle_item(primary_set))
    print(get_middle_item(secondary_set))
    print(get_middle_item(single_set))