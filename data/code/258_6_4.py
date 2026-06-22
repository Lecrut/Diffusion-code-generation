def average_pairs(list1, list2):
    return {pair: (list1[pair[0]] + list2[pair[1]]) / 2 for pair in zip(range(len(list1)), range(len(list2)))}

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    print(average_pairs(sample_list1, sample_list2))