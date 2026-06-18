def is_odd(num):
    return num % 2 != 0 if isinstance(num, int) else False
    
if __name__ == '__main__':
    assert (is_odd(7), True) and (is_odd(8), False) and (is_odd(-3), True)