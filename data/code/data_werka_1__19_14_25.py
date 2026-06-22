def contains_truthy(lst):
    return any(lst)
if __name__ == '__main__':
    sample_list1 = [0, False, None, '', [], {}]
    sample_list2 = [0, False, None, '', [], {}, 1]
    print(contains_truthy(sample_list1))
    print(contains_truthy(sample_list2))