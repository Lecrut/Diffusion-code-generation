def compute_differences(list1, list2):
    differences = {}
    length_limit = min(len(list1), len(list2))
    for index in range(length_limit):
        differences[index] = list1[index] - list2[index]
    return differences

if __name__ == '__main__':
    sample_list_1 = [7, 17, 27, 37]
    sample_list_2 = [4, 8, 12, 16]
    result_differences = compute_differences(sample_list_1, sample_list_2)
    print(result_differences)