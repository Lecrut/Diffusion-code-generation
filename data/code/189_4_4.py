def remove_duplicates(data_list, item_to_remove):
    seen = set()
    result = []
    for item in data_list:
        if item != item_to_remove and item not in seen:
            result.append(item)
            seen.add(item)
    return result
if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    item = 3
    new_list = remove_duplicates(my_list, item)
    print(new_list)
    my_list_2 = ['a', 'b', 'c', 'd', 'e']
    item_2 = 'c'
    new_list_2 = remove_duplicates(my_list_2, item_2)
    print(new_list_2)
    my_list_3 = [10, 20, 30]
    item_3 = 5
    new_list_3 = remove_duplicates(my_list_3, item_3)
    print(new_list_3)