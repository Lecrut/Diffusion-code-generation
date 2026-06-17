class NumberChecker:
    def __init__(self, number):
        self.number = number
    def check_parity(self):
        if self.number % 2 == 0:
            return "Even"
        else:
            return "Odd"
if __name__ == '__main__':
    num1 = 10
    checker1 = NumberChecker(num1)
    print(f"Number {num1} is: {checker1.check_parity()}")
    num2 = 7
    checker2 = NumberChecker(num2)
    print(f"Number {num2} is: {checker2.check_parity()}")
    num3 = 0
    checker3 = NumberChecker(num3)
    print(f"Number {num3} is: {checker3.check_parity()}")
    num4 = -5
    checker4 = NumberChecker(num4)
    print(f"Number {num4} is: {checker4.check_parity()}")