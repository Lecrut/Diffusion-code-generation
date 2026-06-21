def are_lists_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    for index, (item1, item2) in enumerate(zip(list1, list2)):
        if item1 != item2:
            return False
    return True
if __name__ == '__main__':
    first_list = [100, 200, 300, 400]
    second_list = [100, 200, 300, 400]
    third_list = [100, 200, 300, 401]
    print(are_lists_identical(first_list, second_list))
    print(are_lists_identical(first_list, third_list))