class ConditionChecker:
    @staticmethod
    def is_valid(x, y):
        return x > 5 and y < 10

if __name__ == '__main__':
    sample_x = 6
    sample_y = 8
    result = ConditionChecker.is_valid(sample_x, sample_y)
    print(result)