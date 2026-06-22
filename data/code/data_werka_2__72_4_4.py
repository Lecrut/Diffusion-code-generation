def combine_at_index(list1, list2, index):
    if index < 0 or index >= len(list1) or index < 0 or index >= len(list2):
        raise ValueError("Index out of range for one or both lists")
    return [(list1[index], list2[index])]

if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    idx = 1
    result = combine_at_index(list_a, list_b, idx)
    print(result)