def print_common_elements(list1, list2):
    common_elements = set(list1) & set(list2)
    for element in common_elements:
        print(element)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    print_common_elements(list1, list2)