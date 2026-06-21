def pair_elements(list1, list2):
    min_len = min(len(list1), len(list2))
    for i in range(min_len):
        yield (list1[i], list2[i])
if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b']
    pairs = pair_elements(sample_list1, sample_list2)
    for pair in pairs:
        print(pair)