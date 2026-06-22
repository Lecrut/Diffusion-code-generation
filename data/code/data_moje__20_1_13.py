def is_even(n):
    return (n & 1) == 0

if __name__ == '__main__':
    print(is_even(4))
    print(is_even(7))
    print(is_even(0))
    print(is_even(-2))
    print(is_even(100))