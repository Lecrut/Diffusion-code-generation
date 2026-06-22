def find_equal_indices(list1, list2):
    return [i for i, (a, b) in enumerate(zip(list1, list2)) if a == b]

if __name__ == '__main__':
    sample_list1 = [1.1, 2.2, 3.3, 4.4]
    sample_list2 = [1.1, 2.3, 3.3, 4.5]
    print(find_equal_indices(sample_list1, sample_list2))