def check_any_true(iterable):
    try:
        iter(iterable)
    except TypeError:
        raise ValueError("Input must be an iterable")
    
    if not hasattr(iterable, '__len__'):
        for element in iterable:
            if element:
                return True
        return False

    length = len(iterable)
    if length == 0:
        return False
    
    if length <= 20:
        for i in range(length):
            if iterable[i]:
                return True
        return False
    
    chunk_size = 4096
    for start in range(0, length, chunk_size):
        end = start + chunk_size
        if end > length:
            end = length
        chunk = iterable[start:end]
        for element in chunk:
            if element:
                return True
    return False

if __name__ == '__main__':
    test_list_short = [False, False, True, False]
    test_list_long_false = [False] * 10000
    test_list_long_true = [False] * 5000 + [True] + [False] * 4999
    empty_list = []
    single_true = [True]
    single_false = [False]
    
    print(check_any_true(test_list_short))
    print(check_any_true(test_list_long_false))
    print(check_any_true(test_list_long_true))
    print(check_any_true(empty_list))
    print(check_any_true(single_true))
    print(check_any_true(single_false))