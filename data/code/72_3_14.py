def compare_lists(list1, list2):
    for index, (val1, val2) in enumerate(zip(list1, list2)):
        if val1 > val2:
            print(f"List 1 element at index {index} ({val1}) is greater than List 2 element at the same index ({val2})")

if __name__ == '__main__':
    sample_list_a = [5, 10, 15, 20]
    sample_list_b = [3, 10, 14, 25]
    compare_lists(sample_list_a, sample_list_b)