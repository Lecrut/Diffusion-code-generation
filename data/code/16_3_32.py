class NumberChecker:
    def __init__(self, numbers):
        self.numbers = numbers

    def check_all_positive(self):
        return all(num > 0 for num in self.numbers)

if __name__ == '__main__':
    sample_values = [6, 7, 8, 9, 10]
    checker = NumberChecker(sample_values)
    print(checker.check_all_positive())

    sample_values_with_negative = [11, -12, 13, 14, 15]
    negative_checker = NumberChecker(sample_values_with_negative)
    print(negative_checker.check_all_positive())