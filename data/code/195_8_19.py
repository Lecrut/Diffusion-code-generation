def compare_lists(list1, list2):
    return [(i, (a, b)) for i, (a, b) in enumerate(zip(list1, list2)) if a != b]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4]
    sample_list2 = [1, 2, 5, 4]
    differences = compare_lists(sample_list1, sample_list2)
    print(differences)

    sample_list3 = ['a', 'b', 'c']
    sample_list4 = ['a', 'd', 'c']
    differences = compare_lists(sample_list3, sample_list4)
    print(differences)