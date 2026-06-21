class ConditionChecker:
    X_THRESHOLD = 10
    Y_THRESHOLD = 50

    @staticmethod
    def check_conditions(x, y):
        return x > ConditionChecker.X_THRESHOLD and y < ConditionChecker.Y_THRESHOLD

if __name__ == '__main__':
    sample_x = 14
    sample_y = 35
    result = ConditionChecker.check_conditions(sample_x, sample_y)
    print(result)