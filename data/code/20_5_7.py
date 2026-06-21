def check_even(n):
    DIVISOR = 2
    IS_EVEN = "Even"
    IS_ODD = "Odd"
    return IS_EVEN if n % DIVISOR == 0 else IS_ODD

if __name__ == '__main__':
    print(check_even(42))
    print(check_even(7))
    print(check_even(0))
    print(check_even(-13))
    print(check_even(1000))