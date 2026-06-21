def find_large_diff_indices(list1, list2, threshold=0.01):
    return [i for i, (a, b) in enumerate(zip(list1, list2)) if abs(a - b) > threshold]

if __name__ == '__main__':
    sample_list1 = [1.03, 2.04, 3.05, 4.06]
    sample_list2 = [1.00, 2.01, 3.08, 4.07]
    result = find_large_diff_indices(sample_list1, sample_list2)
    print(result)