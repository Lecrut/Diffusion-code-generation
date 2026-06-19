def compute_differences(list1, list2):
    differences = {}
    for i in range(min(len(list1), len(list2))):
        if i not in differences:
            differences[i] = 0
        differences[i] = list1[i] - list2[i]
    return differences

if __name__ == '__main__':
    sample_list_a = [15, 25, 35, 45]
    sample_list_b = [1, 2, 3, 4]
    result = compute_differences(sample_list_a, sample_list_b)
    print(result)