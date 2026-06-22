def extend_with_last_element(lst, n):
    lst.extend([lst[-1]] * n)
    return lst
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    num_copies = 3
    result = extend_with_last_element(sample_list, num_copies)
    print(result)