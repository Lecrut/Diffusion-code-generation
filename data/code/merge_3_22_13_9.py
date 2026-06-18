def check_odd(num):
    return num % 2 != 0 if isinstance(num, int) else False
    
if __name__ == '__main__':
    print(check_odd(7), check_odd(4))