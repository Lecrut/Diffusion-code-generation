def compare_lists(a, b):
    if not isinstance(a, list) or not isinstance(b, list):
        raise ValueError("Both inputs must be lists")
    
    len_a = len(a)
    len_b = len(b)
    
    if len_a > len_b:
        return a
    elif len_b > len_a:
        return b
    else:
        return None

if __name__ == '__main__':
    print(compare_lists([1, 2, 3], [4, 5]))
    print(compare_lists([1, 2], [3, 4, 5]))
    print(compare_lists([1, 2, 3], [4, 5, 6]))
    print(compare_lists([], []))
    print(compare_lists([1, 2, 3], 'not a list'))