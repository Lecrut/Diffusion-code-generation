def have_same_elements(list1, list2):
    return set(list1) == set(list2)
if __name__ == '__main__':
    print(have_same_elements([1, 2, 3], [3, 2, 1]))
    print(have_same_elements([1, 2, 3], [4, 5, 6]))