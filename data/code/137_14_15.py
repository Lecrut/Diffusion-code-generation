class NumberChecker:
    def __init__(self):
        self.sample_numbers = [10, -5, 0, 3.14, -100]

    def is_even(self, number):
        return number & 1 == 0

    def check_number(self, number):
        if number > 0:
            print("Positive")
        elif number < 0:
            print("Negative")
        else:
            print("Zero")

if __name__ == '__main__':
    checker = NumberChecker()
    for num in checker.sample_numbers:
        checker.check_number(num)
        print(f"Number {num} is even: {checker.is_even(num)}")