def lists_have_same_elements(list1, list2):
    return len(set(list1)) == len(set(list2)) and set(list1) & set(list2) == set(list1)
if __name__ == '__main__':
    print(lists_have_same_elements([1, 2, 3], [3, 2, 1]))
    print(lists_have_same_elements([1, 2, 3], [4, 5, 6]))