def remove_item_slice(data_list, item_to_remove):
    try:
        index = data_list.index(item_to_remove)
        result = data_list[:index] + data_list[index+1:]
        return result
    except ValueError:
        return data_list
if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    item = 3
    new_list = remove_item_slice(my_list, item)
    print(new_list)
    my_list_2 = ['a', 'b', 'c', 'd', 'e']
    item_2 = 'c'
    new_list_2 = remove_item_slice(my_list_2, item_2)
    print(new_list_2)
    my_list_3 = [10, 20, 30]
    item_3 = 5                    
    new_list_3 = remove_item_slice(my_list_3, item_3)
    print(new_list_3)