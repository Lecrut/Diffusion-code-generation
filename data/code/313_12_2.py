class NumberChecker:
    def is_even(self, number):
        return number % 2 == 0
if __name__ == '__main__':
    checker = NumberChecker()
    print(f"Is 4 even? {checker.is_even(4)}")
    print(f"Is 7 even? {checker.is_even(7)}")
    print(f"Is 0 even? {checker.is_even(0)}")
    print(f"Is -2 even? {checker.is_even(-2)}")