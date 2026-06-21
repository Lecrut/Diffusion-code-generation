def extend_tuples(list1, list2):
    return list1 + list2

if __name__ == '__main__':
    sample_list1 = [(1, 'a'), (2, 'b')]
    sample_list2 = [(3, 'c'), (4, 'd')]
    result = extend_tuples(sample_list1, sample_list2)
    print(result)