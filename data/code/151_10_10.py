def concatenate_lists(list1, list2):
    return list1 + list2

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result = concatenate_lists(list_a, list_b)
    print(result)