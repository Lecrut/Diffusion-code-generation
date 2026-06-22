class FalseChecker:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_both_false(self):
        return not self.x and not self.y

    def get_values(self):
        return (self.x, self.y)

if __name__ == '__main__':
    checker = FalseChecker(False, False)
    print(checker.is_both_false())
    print(checker.get_values())