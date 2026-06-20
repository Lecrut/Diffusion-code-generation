def is_odd(number: int) -> bool:
    return number & 1 == 1

if __name__ == '__main__':
    num1 = 9
    num2 = 8
    print(f"Is {num1} odd? {is_odd(num1)}")
    print(f"Is {num2} odd? {is_odd(num2)}")