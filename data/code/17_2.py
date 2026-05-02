class NumberChecker:
    def check_parity(self, number):
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"
if __name__ == '__main__':
    checker = NumberChecker()
    num1 = 10
    num2 = 7
    num3 = 0
    num4 = -4
    print(f"Checking {num1}: {checker.check_parity(num1)}")
    print(f"Checking {num2}: {checker.check_parity(num2)}")
    print(f"Checking {num3}: {checker.check_parity(num3)}")
    print(f"Checking {num4}: {checker.check_parity(num4)}")