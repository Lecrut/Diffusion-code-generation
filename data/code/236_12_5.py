def extend_with_last_element(lst, n):
    if not isinstance(lst, list) or not lst:
        raise ValueError("First argument must be a non-empty list.")
    if not isinstance(n, int) or n < 0:
        raise ValueError("Second argument must be a non-negative integer.")
    
    last_element = lst[-1]
    lst.extend([last_element] * n)
    return lst

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    num_copies = 3
    result = extend_with_last_element(sample_list, num_copies)
    print(result)