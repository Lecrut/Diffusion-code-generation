def is_greater(a, b):
    return a > b if a ^ b >= 0 else not b < a
if __name__ == '__main__':
    print(is_greater(5, 3))
    print(is_greater(2, 4))