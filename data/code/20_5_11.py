def check_even(n: int) -> bool:
    return True if n % 2 == 0 else False

if __name__ == '__main__':
    print(check_even(4))
    print(check_even(7))
    print(check_even(0))
    print(check_even(-3))