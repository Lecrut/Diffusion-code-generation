def merge_tuples(list1, list2):
    result = list1.copy()
    result.extend(list2)
    return result

if __name__ == '__main__':
    sample_list1 = [(1, 'x'), (2, 'y')]
    sample_list2 = [(3, 'z'), (4, 'w')]
    merged_result = merge_tuples(sample_list1, sample_list2)
    print(merged_result)