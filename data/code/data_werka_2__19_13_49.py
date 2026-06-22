def contains_truthy(lst):
    has_truthy = False
    for item in lst:
        if item:
            has_truthy = True
            break
    return has_truthy

if __name__ == '__main__':
    sample_list1 = [0, False, None, '']
    sample_list2 = [0, False, None, 42]
    print(contains_truthy(sample_list1))
    print(contains_truthy(sample_list2))