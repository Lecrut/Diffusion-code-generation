class NumberChecker:
    @staticmethod
    def is_positive(n):
        return n > 0

    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def is_divisible_by_three(n):
        return n % 3 == 0

if __name__ == '__main__':
    sample_numbers = [10, 15, -4, 6]
    for number in sample_numbers:
        positive = NumberChecker.is_positive(number)
        even = NumberChecker.is_even(number)
        divisible_by_three = NumberChecker.is_divisible_by_three(number)
        print(f"Number: {number}, Positive: {positive}, Even: {even}, Divisible by 3: {divisible_by_three}")