def remove_item(data_list, item_to_remove):
    return [item for item in data_list if item != item_to_remove]
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
    result_3 = remove_item(my_list_3, item_3)
    print(result_3)