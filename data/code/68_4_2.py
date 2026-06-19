def calculate_differences(list1, list2):
    differences = {}
    for i in range(min(len(list1), len(list2))):
        differences[i] = list1[i] - list2[i]
    return differences

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40]
    sample_list2 = [1, 2, 3, 4]
    result = calculate_differences(sample_list1, sample_list2)
    print(result)