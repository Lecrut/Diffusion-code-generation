def combine_lists(list1, list2):
    return [item for item in list1 for item in list2]
if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined = combine_lists(list1, list2)
    print(combined)