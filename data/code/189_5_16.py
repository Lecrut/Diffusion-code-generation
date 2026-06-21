def safe_remove(data_list):
    if data_list:
        data_list.pop(-1)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    safe_remove(list1)
    print(f"List after removing last element: {list1}")
    empty_list = []
    safe_remove(empty_list)
    print(f"Empty list after attempting to remove last element: {empty_list}")