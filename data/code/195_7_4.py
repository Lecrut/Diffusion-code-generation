def are_permutations(list1, list2):
    return sorted(list1) == sorted(list2)

if __name__ == '__main__':
    sample_list1 = [3, 5, 2, 8]
    sample_list2 = [2, 3, 5, 8]
    print(are_permutations(sample_list1, sample_list2))