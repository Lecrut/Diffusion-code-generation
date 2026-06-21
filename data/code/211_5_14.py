def side_by_side_pairs(list1, list2):
    it1 = iter(list1)
    it2 = iter(list2)
    while True:
        try:
            yield next(it1), next(it2)
        except StopIteration:
            break

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b']
    for pair in side_by_side_pairs(sample_list1, sample_list2):
        print(pair)