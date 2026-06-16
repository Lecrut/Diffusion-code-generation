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
    print(f"{num1} is {checker1.check_parity()}")
    num2 = 7
    checker2 = NumberChecker(num2)
    print(f"{num2} is {checker2.check_parity()}")