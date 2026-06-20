ODD_CHECK_BITMASK = 1

def is_odd(number: int) -> bool:
    return (number & ODD_CHECK_BITMASK) != 0

if __name__ == '__main__':
    num1 = 7
    num2 = 10
    num3 = 0
    num4 = -3
    print(f"Is {num1} odd? {is_odd(num1)}")
    print(f"Is {num2} odd? {is_odd(num2)}")
    print(f"Is {num3} odd? {is_odd(num3)}")
    print(f"Is {num4} odd? {is_odd(num4)}")