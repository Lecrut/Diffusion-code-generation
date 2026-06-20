def is_odd(n: int) -> bool:
    return n & 1

if __name__ == '__main__':
    num1 = 9
    num2 = 14
    num3 = -7
    num4 = 0
    print(f"Is {num1} odd? {is_odd(num1)}")
    print(f"Is {num2} odd? {is_odd(num2)}")
    print(f"Is {num3} odd? {is_odd(num3)}")
    print(f"Is {num4} odd? {is_odd(num4)}")