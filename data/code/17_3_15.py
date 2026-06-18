def check_even(num):
    return num % 2 == 0 if isinstance(num, (int, float)) else False
    
if __name__ == '__main__':
    assert check_even(4) and not check_even(5), "Basic checks failed"