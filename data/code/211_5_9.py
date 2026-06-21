def side_by_side_pairs(list1, list2):
    min_length = min(len(list1), len(list2))
    for i in range(min_length):
        yield (list1[i], list2[i])

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4]
    sample_list2 = ['a', 'b', 'c']
    for pair in side_by_side_pairs(sample_list1, sample_list2):
        print(pair)