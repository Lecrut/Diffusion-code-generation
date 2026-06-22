def get_middle_element(iterable):
    iterator = iter(iterable)
    try:
        middle = next(iterator)
    except StopIteration:
        raise ValueError("Input iterable is empty")
    
    second = next(iterator, None)
    if second is None:
        return middle
    
    count = 2
    while True:
        current = next(iterator, None)
        if current is None:
            break
        if count % 2 == 0:
            middle = second
        second = current
        count += 1
    
    if count % 2 == 0:
        return second
    return middle

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_middle_element(sample_list)
    print(result)
    
    sample_tuple = (1, 2, 3)
    result2 = get_middle_element(sample_tuple)
    print(result2)
    
    sample_range = range(10)
    result3 = get_middle_element(sample_range)
    print(result3)