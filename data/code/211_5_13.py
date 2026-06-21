def pair_elements(list1, list2):
    min_length = min(len(list1), len(list2))
    for i in range(min_length):
        yield (list1[i], list2[i])

if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = ['a', 'b', 'c']
    paired_elements = pair_elements(sample_list1, sample_list2)
    for pair in paired_elements:
        print(pair)