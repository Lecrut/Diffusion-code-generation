def any_truthy(iterable):
    for item in iterable:
        if item:
            return True
    return False

if __name__ == '__main__':
    result1 = any_truthy([False, False, True])
    print(result1)
    
    result2 = any_truthy([False, False, False])
    print(result2)
    
    result3 = any_truthy([])
    print(result3)