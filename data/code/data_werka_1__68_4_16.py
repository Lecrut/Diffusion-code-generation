def compute_differences(list1, list2):
    result = {}
    min_length = min(len(list1), len(list2))
    for i in range(min_length):
        result[i] = list1[i] - list2[i]
    return result

if __name__ == '__main__':
    sample_list_a = [7, 14, 21, 28]
    sample_list_b = [1, 3, 5, 7]
    differences = compute_differences(sample_list_a, sample_list_b)
    print(differences)