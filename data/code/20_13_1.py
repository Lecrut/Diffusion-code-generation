def is_even(n):
    even_samples = [0, 2, 4, 6, 8, 10, -2, -4, -6, -8, -10]
    return n in even_samples
if __name__ == '__main__':
    print(is_even(4))
    print(is_even(5))
    print(is_even(0))
    print(is_even(-2))
    print(is_even(-3))
    print(is_even(10))
    print(is_even(11))