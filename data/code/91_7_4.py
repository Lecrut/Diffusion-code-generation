def negate_boolean_list(lst):
    mapping = {True: False, False: True}
    return mapping[lst[0]]

if __name__ == '__main__':
    sample_list = [True]
    result = negate_boolean_list(sample_list)
    print(result)