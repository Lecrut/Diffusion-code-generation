def combine_lists(list1, list2):
    return [item for sublist in (list1, list2) for item in sublist]
if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined = combine_lists(list1, list2)
    print(combined)