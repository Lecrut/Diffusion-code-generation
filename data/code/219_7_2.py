def find_max_pairs(list1, list2):
    max_values = [max(a, b) for a, b in zip(list1, list2)]
    return max_values

if __name__ == '__main__':
    sample_list1 = [7, 9, 2]
    sample_list2 = [5, 8, 4]
    result = find_max_pairs(sample_list1, sample_list2)
    print(result)