def are_lists_identical(list1, list2):
    length1 = len(list1)
    length2 = len(list2)
    if length1 != length2:
        return False
    for index in range(length1):
        if list1[index] != list2[index]:
            return False
    return True
if __name__ == '__main__':
    first_list = [15, 25, 35, 45, 55]
    second_list = [15, 25, 35, 45, 55]
    third_list = [15, 25, 35, 45, 65]
    result1 = are_lists_identical(first_list, second_list)
    result2 = are_lists_identical(first_list, third_list)
    print(result1)
    print(result2)