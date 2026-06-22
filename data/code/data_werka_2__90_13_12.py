import numbers

def check_either_exceeds_threshold(val_one, val_two):
    if not isinstance(val_one, numbers.Integral):
        raise ValueError("First argument must be an integer")
    if not isinstance(val_two, numbers.Integral):
        raise ValueError("Second argument must be an integer")
    
    threshold = 10
    is_first_greater = val_one > threshold
    is_second_greater = val_two > threshold
    
    return is_first_greater or is_second_greater

if __name__ == '__main__':
    a = 7
    b = 11
    result = check_either_exceeds_threshold(a, b)
    print(result)