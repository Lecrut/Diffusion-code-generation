def remove_item(original_list, item_to_remove):
    new_list = [x for x in original_list if x != item_to_remove]
    return new_list
if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 2, 5]
    item = 2
    new_list = remove_item(my_list, item)
    print(f"Original list: {my_list}")
    print(f"Item to remove: {item}")
    print(f"New list: {new_list}")