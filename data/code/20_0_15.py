class EvenChecker:
    def __init__(self, value):
        self.value = value

    def is_even(self):
        return self.value % 2 == 0

if __name__ == '__main__':
    checker1 = EvenChecker(10)
    print(checker1.is_even())
    checker2 = EvenChecker(7)
    print(checker2.is_even())
    checker3 = EvenChecker(-4)
    print(checker3.is_even())
    checker4 = EvenChecker(0)
    print(checker4.is_even())