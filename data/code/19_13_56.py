def contains_truthy(lst):
    return any(lst)
if __name__ == '__main__':
    sample_list_1 = [False, 0, None, '', [], {}]
    sample_list_2 = [False, 0, None, '', [], {}, 42]
    print(contains_truthy(sample_list_1))
    print(contains_truthy(sample_list_2))