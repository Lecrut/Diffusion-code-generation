def get_middle(iterable):
    try:
        iterator = iter(iterable)
    except TypeError:
        raise ValueError("Input must be iterable")
    
    left = next(iterator, None)
    if left is None:
        raise ValueError("Input iterable is empty")
    
    right = next(iterator, None)
    if right is None:
        return left
    
    while True:
        left = next(iterator, None)
        if left is None:
            return right
        right = next(iterator, None)
        if right is None:
            return left

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_middle(sample_list)
    print(result)
    
    sample_tuple = ('a', 'b', 'c', 'd')
    result2 = get_middle(sample_tuple)
    print(result2)
    
    sample_single = [99]
    result3 = get_middle(sample_single)
    print(result3)