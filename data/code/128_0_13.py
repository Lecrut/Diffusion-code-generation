class NumberChecker:
    def __init__(self, number):
        self.number = number

    def is_negative(self):
        return self.number < 0

if __name__ == '__main__':
    checker1 = NumberChecker(-10)
    print(f"Is -10 negative? {checker1.is_negative()}")

    checker2 = NumberChecker(5)
    print(f"Is 5 negative? {checker2.is_negative()}")