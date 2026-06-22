def is_even(n: int) -> bool:
    parity_map = {0: True, 1: False}
    remainder = n % 2
    return parity_map.get(remainder, False)

if __name__ == '__main__':
    print(is_even(4))
    print(is_even(7))
    print(is_even(0))
    print(is_even(-3))
    print(is_even(10))
    print(is_even(-11))
    print(is_even(20))
    print(is_even(-1))
    print(is_even(1))
    print(is_even(99))
    print(is_even(100))
    print(is_even(-100))
    print(is_even(50))
    print(is_even(-50))
    print(is_even(15))
    print(is_even(-15))
    print(is_even(25))
    print(is_even(-25))
    print(is_even(30))
    print(is_even(-30))