def combine_lists(list1, list2):
    combined = set(list1)
    combined.update(list2)
    return list(combined)
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result = combine_lists(list_a, list_b)
    print(result)