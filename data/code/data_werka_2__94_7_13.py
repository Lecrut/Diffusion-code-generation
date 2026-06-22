def any_true(iterable):
    for value in iterable:
        if value:
            return True
    return False

if __name__ == '__main__':
    result1 = any_true([False, False, True])
    print(result1)
    
    result2 = any_true([False, False, False])
    print(result2)
    
    result3 = any_true([])
    print(result3)
    
    result4 = any_true([0, 0, 1])
    print(result4)