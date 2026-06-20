class NegativeChecker:
    @staticmethod
    def is_negative(number):
        return number < 0

if __name__ == '__main__':
    checker = NegativeChecker()
    print(f"is_negative(-5): {checker.is_negative(-5)}")
    print(f"is_negative(0): {checker.is_negative(0)}")
    print(f"is_negative(10.5): {checker.is_negative(10.5)}")
    print(f"is_negative(-0.001): {checker.is_negative(-0.001)}")