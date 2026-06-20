def verify_oddity(n):
    if not isinstance(n, int):
        raise TypeError('Input must be an integer')
    return n & 1 == 1
if __name__ == '__main__':
    print(verify_oddity(3))
    print(verify_oddity(4))