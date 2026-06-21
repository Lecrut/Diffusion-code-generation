def contains_truthy(lst):
    if not isinstance(lst, list):
        raise ValueError('Input must be a list')
    return any(map(bool, lst))
if __name__ == '__main__':
    sample_list1 = [0, False, None, '']
    sample_list2 = [0, False, None, 'hello']
    sample_list3 = []
    sample_list4 = [None, 0, False, 0.0, '', [], {}]
    print(contains_truthy(sample_list1))
    print(contains_truthy(sample_list2))
    print(contains_truthy(sample_list3))
    print(contains_truthy(sample_list4))
    try:
        contains_truthy('not a list')
    except ValueError as e:
        print(e)