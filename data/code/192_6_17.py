def intersect_lists(list1, list2):
    return list(filter(lambda x: isinstance(x, (int, float, str)) and x in set(list2), list1))

if __name__ == '__main__':
    sample_list1 = [1, 'a', 3.5, 4, (1, 2)]
    sample_list2 = [3.5, 4, 5, 'b']
    result = intersect_lists(sample_list1, sample_list2)
    print(result)