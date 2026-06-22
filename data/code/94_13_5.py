def any_truthy(sequence):
    truthy_map = {
        'empty': False,
        'single': False,
        'multiple': False,
    }
    
    iterator = iter(sequence)
    
    try:
        first = next(iterator)
    except StopIteration:
        return truthy_map['empty']
        
    if first:
        return True
        
    for item in iterator:
        if item:
            return True
            
    return False

if __name__ == '__main__':
    test_data = [0, None, False, 42, 0]
    result = any_truthy(test_data)
    print(result)
    
    empty_data = []
    empty_result = any_truthy(empty_data)
    print(empty_result)
    
    all_false_data = [0, False, None, '']
    all_false_result = any_truthy(all_false_data)
    print(all_false_result)