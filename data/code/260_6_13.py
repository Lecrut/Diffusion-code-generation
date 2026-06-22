def compare_lists(list1, list2):
    return [i for i, (a, b) in enumerate(zip(list1, list2)) if a == b]

if __name__ == '__main__':
    sample_list1 = [1.0, 2.5, 3.0, 4.5]
    sample_list2 = [1.0, 2.6, 3.0, 4.5]
    print(compare_lists(sample_list1, sample_list2))