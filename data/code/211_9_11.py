def find_large_diff_indices(list1, list2):
    threshold = 0.01
    indices = [i for i in range(len(list1)) if abs(list1[i] - list2[i]) > threshold]
    return indices

if __name__ == '__main__':
    sample_list1 = [1.01, 2.02, 3.03, 4.04, 5.05]
    sample_list2 = [1.00, 2.03, 3.02, 4.06, 5.04]
    result = find_large_diff_indices(sample_list1, sample_list2)
    print(result)