def is_odd(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    return n & 1

if __name__ == '__main__':
    num1 = 7
    num2 = 10
    num3 = 0
    print(f"Is {num1} odd? {is_odd(num1)}")
    print(f"Is {num2} odd? {is_odd(num2)}")
    print(f"Is {num3} odd? {is_odd(num3)}")