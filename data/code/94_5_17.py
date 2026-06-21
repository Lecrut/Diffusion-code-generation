def has_true(sequence):
    if not hasattr(sequence, '__iter__'):
        raise ValueError("Input must be iterable")
    for element in sequence:
        if element is True or element == True:
            yield True
            return
    yield False

if __name__ == '__main__':
    data1 = [False, False, True, False]
    result1 = next(has_true(data1))
    print(result1)
    
    data2 = [False, False, False]
    result2 = next(has_true(data2))
    print(result2)
    
    data3 = [True, False, True]
    result3 = next(has_true(data3))
    print(result3)