def is_odd_bitwise(n):
    return (n & 1) == 1
if __name__ == '__main__':
    number1 = 7
    number2 = 10
    number3 = 0
    number4 = -5
    print(f"Is {number1} odd? {is_odd_bitwise(number1)}")
    print(f"Is {number2} odd? {is_odd_bitwise(number2)}")
    print(f"Is {number3} odd? {is_odd_bitwise(number3)}")
    print(f"Is {number4} odd? {is_odd_bitwise(number4)}")