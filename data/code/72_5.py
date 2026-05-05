def combine_lists_at_index(list1, list2, index):
    result = [(list1[index], list2[index])]
    return result
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [10, 20, 30, 40]
    idx = 1
    output = combine_lists_at_index(list_a, list_b, idx)
    print(output)