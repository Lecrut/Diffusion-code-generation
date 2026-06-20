class ConditionChecker:
    @staticmethod
    def is_x_greater_than_five(x):
        return x > 5

    @staticmethod
    def is_y_less_than_ten(y):
        return y < 10

    @classmethod
    def check_combined_conditions(cls, x, y):
        return cls.is_x_greater_than_five(x) and cls.is_y_less_than_ten(y)

if __name__ == '__main__':
    result = ConditionChecker.check_combined_conditions(6, 8)
    print(result)