def is_greater(a, b):
    return (a > 0) ^ ((a ^ b) & a < 0)
if __name__ == '__main__':
    print(is_greater(5, 3))
    print(is_greater(2, 4))