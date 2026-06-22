def find_equal_indices(list1, list2):
    return [i for i, (a, b) in enumerate(zip(list1, list2)) if a == b]

if __name__ == '__main__':
    sample_list1 = [1.0, 2.5, 3.3, 4.7]
    sample_list2 = [1.0, 2.6, 3.3, 4.8]
    print(find_equal_indices(sample_list1, sample_list2))