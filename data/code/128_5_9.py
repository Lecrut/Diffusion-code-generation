class NegativeChecker:
    def __init__(self, data):
        self.data = data

    def has_negative(self):
        return any(x < 0 for x in self.data)

if __name__ == '__main__':
    checker = NegativeChecker([-1, 2, 3, -4, 5])
    print(checker.has_negative())