def are_permutations(list1, list2):
    if len(list1) != len(list2):
        return False
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    return sorted_list1 == sorted_list2

if __name__ == '__main__':
    sample_list1 = [3, 5, 2, 8]
    sample_list2 = [2, 5, 3, 8]
    print(are_permutations(sample_list1, sample_list2))