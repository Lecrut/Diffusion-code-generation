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
    print(f"Parity of {num1}: {checker.check_parity(num1)}")
    print(f"Parity of {num2}: {checker.check_parity(num2)}")
    print(f"Parity of {num3}: {checker.check_parity(num3)}")