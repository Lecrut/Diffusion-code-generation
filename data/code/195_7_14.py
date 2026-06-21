def are_permutations(list1, list2):
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    return sorted_list1 == sorted_list2

if __name__ == '__main__':
    sample_list1 = [9, 7, 5, 3]
    sample_list2 = [3, 5, 7, 9]
    result = are_permutations(sample_list1, sample_list2)
    print(result)