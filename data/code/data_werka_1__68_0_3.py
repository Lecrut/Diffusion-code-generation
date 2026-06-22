def calculate_differences(list1, list2):
    min_length = min(len(list1), len(list2))
    differences = []
    for i in range(min_length):
        diff = list1[i] - list2[i]
        differences.append(diff)
    return sum(differences)

if __name__ == '__main__':
    sample_list1 = [7, 14, 21, 28]
    sample_list2 = [1, 3, 5, 7]
    result = calculate_differences(sample_list1, sample_list2)
    print(result)