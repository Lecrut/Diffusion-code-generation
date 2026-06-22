def compute_differences(list1, list2):
    differences = {}
    min_length = min(len(list1), len(list2))
    for index in range(min_length):
        differences[index] = list1[index] - list2[index]
    return differences

if __name__ == '__main__':
    sample_list_1 = [5, 15, 25, 35]
    sample_list_2 = [3, 6, 9, 12]
    result_differences = compute_differences(sample_list_1, sample_list_2)
    print(result_differences)