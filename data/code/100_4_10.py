class ConditionEvaluator:
    @staticmethod
    def is_greater(x, y):
        return x > y

if __name__ == '__main__':
    sample_x = 7
    sample_y = 5
    result = ConditionEvaluator.is_greater(sample_x, sample_y)
    print(f"Sample X: {sample_x}")
    print(f"Sample Y: {sample_y}")
    print(f"Is Greater: {result}")