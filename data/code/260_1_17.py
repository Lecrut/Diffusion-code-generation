def find_common_elements(list1, list2):
    return [value for value in list1 if value in list2]

if __name__ == '__main__':
    list_a = [1, 5, 3, 7]
    list_b = [2, 4, 6, 1]
    common_elements = find_common_elements(list_a, list_b)
    print(common_elements)