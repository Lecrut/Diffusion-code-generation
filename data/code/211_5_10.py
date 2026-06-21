def side_by_side_pairs(list1, list2):
    length = min(len(list1), len(list2))
    for i in range(length):
        yield (list1[i], list2[i])

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    for pair in side_by_side_pairs(list_a, list_b):
        print(pair)