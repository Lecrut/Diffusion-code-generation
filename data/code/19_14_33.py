def has_truthy_element(lst):
    return any(lst)
if __name__ == '__main__':
    sample_list_1 = [0, False, None, '', [], {}]
    sample_list_2 = [0, False, None, '', [], {}, 1]
    print(has_truthy_element(sample_list_1))
    print(has_truthy_element(sample_list_2))