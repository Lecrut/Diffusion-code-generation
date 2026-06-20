class NumberChecker:
    def __init__(self, number):
        self.number = number

    def is_positive(self):
        return self.number > 0

    def is_even(self):
        return self.number % 2 == 0

    def is_divisible_by_three(self):
        return self.number % 3 == 0

if __name__ == '__main__':
    sample_numbers = [10, 15, -4, 6]
    for number in sample_numbers:
        checker = NumberChecker(number)
        print(f"Number: {number}, Positive: {checker.is_positive()}, Even: {checker.is_even()}, Divisible by 3: {checker.is_divisible_by_three()}")