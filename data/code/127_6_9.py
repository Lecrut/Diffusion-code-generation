def is_integer(value):
    return isinstance(value, int)

def verify_oddity(number):
    if not is_integer(number):
        raise ValueError('Input must be an integer')
    return number % 2 != 0
if __name__ == '__main__':
    print(verify_oddity(3))
    print(verify_oddity(4))
    print(verify_oddity(-5))
    print(verify_oddity(0))