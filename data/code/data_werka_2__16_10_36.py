class PositiveChecker:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be an integer or float")
        self.value = value

    def is_positive(self):
        return self.value > 0

if __name__ == '__main__':
    checker1 = PositiveChecker(5)
    print(checker1.is_positive())

    checker2 = PositiveChecker(-3)
    print(checker2.is_positive())

    checker3 = PositiveChecker(0)
    print(checker3.is_positive())