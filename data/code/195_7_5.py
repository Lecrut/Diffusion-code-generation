def are_permutations(list1, list2):
    return sorted(list1) == sorted(list2)

if __name__ == '__main__':
    sample_list1 = [3, 5, 2, 8]
    sample_list2 = [8, 2, 5, 3]
    print(are_permutations(sample_list1, sample_list2))