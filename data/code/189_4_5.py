def remove_item(data_list, item_to_remove):
    if not isinstance(data_list, list) or not all((isinstance(x, (int, str)) for x in data_list)):
        raise ValueError('First argument must be a list of integers and/or strings.')
    try:
        index = data_list.index(item_to_remove)
        new_list = data_list[:index] + data_list[index + 1:]
        return new_list
    except ValueError:
        return data_list
if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    item = 3
    result = remove_item(my_list, item)
    print(result)
    my_list_2 = ['a', 'b', 'c', 'd', 'e']
    item_2 = 'c'
    result_2 = remove_item(my_list_2, item_2)
    print(result_2)
    my_list_3 = [10, 20, 30]
    item_3 = 5
    try:
        result_3 = remove_item(my_list_3, item_3)
        print(result_3)
    except ValueError as e:
        print(e)