def find_last_index(data, value):

    def is_valid_data(data):
        return isinstance(data, list)

    def is_valid_value(value):
        return True
    if not is_valid_data(data) or not is_valid_value(value):
        raise ValueError('Invalid input data or value')
    last_index = -1
    for i in range(len(data) - 1, -1, -1):
        if data[i] == value:
            last_index = i
            break
    return last_index
if __name__ == '__main__':
    list1 = [3, 6, 9, 6, 12, 6]
    value1 = 6
    result1 = find_last_index(list1, value1)
    print(f'List: {list1}, Value: {value1}, Last Index: {result1}')
    list2 = [7, 14, 21, 14, 28]
    value2 = 14
    result2 = find_last_index(list2, value2)
    print(f'List: {list2}, Value: {value2}, Last Index: {result2}')
    list3 = [15, 30, 45, 60]
    value3 = 75
    result3 = find_last_index(list3, value3)
    print(f'List: {list3}, Value: {value3}, Last Index: {result3}')