class NumberChecker:
    def check_negativity(self, value):
        return value < 0

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = [-10, 0, 5, -3.5]
    for val in sample_values:
        print(checker.check_negativity(val))