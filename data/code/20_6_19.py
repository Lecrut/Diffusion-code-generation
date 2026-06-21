def is_even(n):
    return not (n & 1)

if __name__ == '__main__':
    print(is_even(4))
    print(is_even(7))
    print(is_even(0))