def check_any_true(iterable):
    if not hasattr(iterable, '__iter__'):
        raise ValueError("Input must be an iterable")
    
    iterator = iter(iterable)
    
    while True:
        try:
            item = next(iterator)
            if item:
                return True
        except StopIteration:
            return False

if __name__ == '__main__':
    data1 = [False, False, True, False]
    data2 = [False, False, False]
    data3 = [True]
    data4 = []
    data5 = [False, False, False, False]
    
    print(check_any_true(data1))
    print(check_any_true(data2))
    print(check_any_true(data3))
    print(check_any_true(data4))
    print(check_any_true(data5))