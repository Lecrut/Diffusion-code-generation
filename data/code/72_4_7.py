def combine_at_index(list1, list2, index):
    if index < 0 or index >= len(list1) or index < 0 or index >= len(list2):
        raise ValueError("Index out of range for one or both lists")
    return [(list1[index], list2[index])]

if __name__ == '__main__':
    result = combine_at_index([1, 2, 3], [4, 5, 6], 1)
    print(result)