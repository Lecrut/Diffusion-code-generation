def side_by_side_pairs(list1, list2):
    return ((x, y) for x, y in zip(list1, list2))

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b']
    for pair in side_by_side_pairs(sample_list1, sample_list2):
        print(pair)