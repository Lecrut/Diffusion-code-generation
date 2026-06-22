def find_last_index(data, value):
    if not isinstance(data, list):
        raise TypeError("The first argument must be a list.")
    last_index = -1
    for i in range(len(data) - 1, -1, -1):
        if data[i] == value:
            last_index = i
            break
    return last_index

if __name__ == '__main__':
    try:
        sample_list1 = [3, 7, 5, 7, 9, 7]
        target_value1 = 7
        print(find_last_index(sample_list1, target_value1))

        sample_list2 = ['a', 'b', 'c', 'b', 'd']
        target_value2 = 'b'
        print(find_last_index(sample_list2, target_value2))

        sample_list3 = [10, 20, 30, 40]
        target_value3 = 50
        print(find_last_index(sample_list3, target_value3))
    except Exception as e:
        print(e)