class OddChecker:
    def __init__(self, num):
        self.num = num

    def is_odd(self):
        return self.num % 2 != 0

if __name__ == '__main__':
    checker = OddChecker(17)
    print(checker.is_odd())