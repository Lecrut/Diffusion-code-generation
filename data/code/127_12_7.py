IS_ODD_MASK = 1

def is_odd(number: int) -> bool:
    return (number & IS_ODD_MASK) != 0

if __name__ == '__main__':
    print(is_odd(7))  # True
    print(is_odd(10))  # False
    print(is_odd(0))  # False
    print(is_odd(-3))  # True