ODD_CHECK = 1

def is_odd(n):
    return n & ODD_CHECK

if __name__ == '__main__':
    num1 = 10
    num2 = 7
    num3 = 0
    print(f"Is {num1} odd? {is_odd(num1)}")
    print(f"Is {num2} odd? {is_odd(num2)}")
    print(f"Is {num3} odd? {is_odd(num3)}")