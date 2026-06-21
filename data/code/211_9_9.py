def compare_lists(list1, list2):
    return [i for i, (a, b) in enumerate(zip(list1, list2)) if abs(a - b) > 0.01]

if __name__ == '__main__':
    sample_list1 = [1.01, 2.02, 3.03, 4.04]
    sample_list2 = [1.00, 2.03, 3.02, 4.05]
    result = compare_lists(sample_list1, sample_list2)
    print(result)