def average_pairs(list1, list2):
    return {list1[i]: (list1[i] + list2[i]) / 2 for i in range(min(len(list1), len(list2)))}

if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = [5, 15, 25]
    print(average_pairs(sample_list1, sample_list2))