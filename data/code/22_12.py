class NumberChecker:
    def check_odd(self, number):
        return number % 2 != 0
if __name__ == '__main__':
    checker = NumberChecker()
    num1 = 7
    num2 = 10
    num3 = 15
    print(f"Is {num1} odd? {checker.check_odd(num1)}")
    print(f"Is {num2} odd? {checker.check_odd(num2)}")
    print(f"Is {num3} odd? {checker.check_odd(num3)}")