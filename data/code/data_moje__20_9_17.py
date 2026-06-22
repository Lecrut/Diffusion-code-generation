def is_even(n):
    return (n & 1) == 0

if __name__ == '__main__':
    print(is_even(10))
    print(is_even(7))