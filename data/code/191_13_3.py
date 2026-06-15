def combine_lists(list1, list2):
    return [item for item in list1] + [item for item in list2]
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [5, 6, 7, 8]
    combined = combine_lists(list_a, list_b)
    print(combined)