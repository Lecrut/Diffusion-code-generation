class NumberChecker:
    def __init__(self, value):
        self.value = value

    def is_zero(self):
        return self.value == 0

if __name__ == '__main__':
    sample_value = 0
    checker = NumberChecker(sample_value)
    print(checker.is_zero())