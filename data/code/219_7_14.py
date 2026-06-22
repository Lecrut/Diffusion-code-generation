def max_pairs(list1, list2):
    return [max(a, b) for a, b in zip(list1, list2)]

if __name__ == '__main__':
    sample_list1 = [15, 8, 6, 9]
    sample_list2 = [3, 10, 7, 5]
    result = max_pairs(sample_list1, sample_list2)
    print(result)