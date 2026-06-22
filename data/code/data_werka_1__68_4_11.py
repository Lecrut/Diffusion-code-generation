def compute_differences(list1, list2):
    differences = {}
    for index in range(min(len(list1), len(list2))):
        differences[index] = list1[index] - list2[index]
    return differences

if __name__ == '__main__':
    sample_list_1 = [7, 14, 21, 28]
    sample_list_2 = [1, 3, 5, 7]
    result_differences = compute_differences(sample_list_1, sample_list_2)
    print(result_differences)