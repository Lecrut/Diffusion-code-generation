ODD_THRESHOLD = 1

def is_odd(number):
    return number % 2 != ODD_THRESHOLD

if __name__ == '__main__':
    print(is_odd(3))
    print(is_odd(-4))
    print(is_odd(0))
    print(is_odd(17))