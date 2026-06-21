class ConditionChecker:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("Both x and y must be numbers.")
        self.x = x
        self.y = y

    def check_condition(self):
        return self.x > 10 and self.y < 50

if __name__ == '__main__':
    try:
        checker = ConditionChecker(25, 49)
        result = checker.check_condition()
        print(result)
    except ValueError as e:
        print(e)