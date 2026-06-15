def remove_with_list_remove(data_list, item):
    try:
        data_list.remove(item)
        return True
    except ValueError:
        return False
def remove_with_del(data_list, index):
    try:
        del data_list[index]
        return True
    except IndexError:
        return False
if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    print("Original list:", my_list)
    item_to_remove_present = 30
    print(f"\nAttempting to remove {item_to_remove_present} using list.remove():")
    success_remove = remove_with_list_remove(my_list, item_to_remove_present)
    print("Removal successful:", success_remove)
    print("List after removing present item:", my_list)
    item_to_remove_absent = 99
    print(f"\nAttempting to remove {item_to_remove_absent} using list.remove():")
    success_remove_fail = remove_with_list_remove(my_list, item_to_remove_absent)
    print("Removal successful:", success_remove_fail)
    print("List after failed removal attempt:", my_list)
    index_to_delete_valid = 1
    print(f"\nAttempting to delete element at index {index_to_delete_valid} using del:")
    success_del = remove_with_del(my_list, index_to_delete_valid)
    print("Deletion successful:", success_del)
    print("List after deleting valid index:", my_list)
    index_to_delete_invalid = 100
    print(f"\nAttempting to delete element at index {index_to_delete_invalid} using del:")
    success_del_fail = remove_with_del(my_list, index_to_delete_invalid)
    print("Deletion successful:", success_del_fail)
    print("List after failed deletion attempt:", my_list)