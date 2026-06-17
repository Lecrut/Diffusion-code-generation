class NumberChecker:
    def is_even(self, number):
        return number % 2 == 0
if __name__ == '__main__':
    checker = NumberChecker()
    num1 = 4
    num2 = 7
    num3 = 0
    num4 = -2
    print(f"Is {num1} even? {checker.is_even(num1)}")
    print(f"Is {num2} even? {checker.is_even(num2)}")
    print(f"Is {num3} even? {checker.is_even(num3)}")
    print(f"Is {num4} even? {checker.is_even(num4)}")