def compute_differences(list1, list2):
    differences = {}
    for index in range(min(len(list1), len(list2))):
        differences[index] = list1[index] - list2[index]
    return differences

if __name__ == '__main__':
    sample_list_a = [8, 16, 24, 32]
    sample_list_b = [2, 4, 6, 8]
    result_differences = compute_differences(sample_list_a, sample_list_b)
    print(result_differences)