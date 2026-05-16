class NumberChecker:
    def is_odd(self, number):
        return number % 2 != 0
if __name__ == '__main__':
    checker = NumberChecker()
    num1 = 7
    num2 = 10
    num3 = 0
    num4 = -5
    print(f"Is {num1} odd? {checker.is_odd(num1)}")
    print(f"Is {num2} odd? {checker.is_odd(num2)}")
    print(f"Is {num3} odd? {checker.is_odd(num3)}")
    print(f"Is {num4} odd? {checker.is_odd(num4)}")