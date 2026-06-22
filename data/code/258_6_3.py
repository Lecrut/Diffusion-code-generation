def average_pairs(list1, list2):
    return {pair[0]: (pair[1] + pair[2]) / 2 for pair in zip(list1, list2)}

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    result = average_pairs(sample_list1, sample_list2)
    print(result)