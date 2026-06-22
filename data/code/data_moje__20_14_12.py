def is_even(n):
    if not isinstance(n, int) or isinstance(n, bool):
        return "Error: Input must be an integer"
    return n % 2 == 0

if __name__ == '__main__':
    print(is_even(4))
    print(is_even(3))
    print(is_even("hello"))
    print(is_even(2.5))
    print(is_even(True))