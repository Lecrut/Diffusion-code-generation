def sum_of_differences(list1, list2):
    min_length = min(len(list1), len(list2))
    differences = [list1[i] - list2[i] for i in range(min_length)]
    return sum(differences)

if __name__ == '__main__':
    sample_list1 = [5, 10, 15, 20]
    sample_list2 = [3, 8, 13, 18, 23]
    result = sum_of_differences(sample_list1, sample_list2)
    print(result)