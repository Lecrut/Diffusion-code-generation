def compute_indexed_differences(list1, list2):
    result = {}
    length_min = min(len(list1), len(list2))
    for i in range(length_min):
        difference = list1[i] - list2[i]
        result[i] = difference
    return result

if __name__ == '__main__':
    sample_list_1 = [7, 14, 21, 28]
    sample_list_2 = [1, 3, 5, 7]
    differences_result = compute_indexed_differences(sample_list_1, sample_list_2)
    print(differences_result)