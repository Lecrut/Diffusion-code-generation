def extend_with_last_element(lst, n):
    if not lst or n <= 0:
        return lst
    last_element = lst[-1]
    lst.extend([last_element] * (n - 1))
    return lst
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    num_copies = 3
    result = extend_with_last_element(sample_list, num_copies)
    print(result)