EVEN_ODD_MAP = {0: True, 1: False}

def is_even(n):
    return EVEN_ODD_MAP[n % 2]
if __name__ == '__main__':
    print(is_even(10))
    print(is_even(3))