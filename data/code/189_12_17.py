def remove_by_index(data_list, index):
    if not isinstance(data_list, list) or not isinstance(index, int):
        raise TypeError('Invalid input types')
    if index < 0 or index >= len(data_list):
        raise IndexError('Index out of range')
    del data_list[index]
if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    try:
        remove_by_index(my_list, 2)
        print(my_list)
    except Exception as e:
        print(e)
    try:
        remove_by_index(my_list, 5)
    except Exception as e:
        print(e)
    try:
        remove_by_index('not a list', 0)
    except Exception as e:
        print(e)