class NumberChecker:

    def __init__(self, number):
        self.number = number

    def is_negative(self):
        return self.number < 0
if __name__ == '__main__':
    checker1 = NumberChecker(-5)
    print(checker1.is_negative())
    checker2 = NumberChecker(0)
    print(checker2.is_negative())
    checker3 = NumberChecker(3)
    print(checker3.is_negative())