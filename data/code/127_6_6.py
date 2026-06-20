def verify_oddity(num):
    if not isinstance(num, int):
        raise TypeError('Input must be an integer')
    return num & 1 == 1
if __name__ == '__main__':
    print(verify_oddity(3))
    print(verify_oddity(4))