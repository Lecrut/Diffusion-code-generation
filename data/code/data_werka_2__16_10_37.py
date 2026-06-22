class PositiveChecker:
    def __init__(self, value):
        self.value = value

    def is_positive(self):
        return self.value > 0

if __name__ == '__main__':
    checker1 = PositiveChecker(7)
    checker2 = PositiveChecker(-3)
    checker3 = PositiveChecker(0)

    print(checker1.is_positive())
    print(checker2.is_positive())
    print(checker3.is_positive())