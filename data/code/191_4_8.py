sample_list1 = [(1, 2), (3, 4)]
sample_list2 = [(5, 6), (7, 8)]

def extend_tuples(list1, list2):
    return list1 + list2

if __name__ == '__main__':
    result = extend_tuples(sample_list1, sample_list2)
    print(result)