def merge_tuples(list1, list2):
    merged_list = list1[:]
    for item in list2:
        merged_list.append(item)
    return merged_list

if __name__ == '__main__':
    sample_list1 = [(1, 'x'), (2, 'y')]
    sample_list2 = [(3, 'z'), (4, 'w')]
    result = merge_tuples(sample_list1, sample_list2)
    print(result)