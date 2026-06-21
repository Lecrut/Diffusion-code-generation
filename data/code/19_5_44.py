class ConditionChecker:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_x_greater_than_10(self):
        return self.x > 10

    def is_y_less_than_50(self):
        return self.y < 50

    def evaluate_condition(self):
        return self.is_x_greater_than_10() and self.is_y_less_than_50()
if __name__ == '__main__':
    checker = ConditionChecker(11, 49)
    print(checker.is_x_greater_than_10())
    print(checker.is_y_less_than_50())
    print(checker.evaluate_condition())