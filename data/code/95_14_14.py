class ConditionChecker:
    THRESHOLD_ZERO = 0.0

    @staticmethod
    def check_conditions(first: float, second: float, third: float) -> bool:
        is_positive = first > ConditionChecker.THRESHOLD_ZERO
        is_less = second < first
        is_sum = third == first + second
        return is_positive and is_less and is_sum

if __name__ == '__main__':
    result = ConditionChecker.check_conditions(5.0, 2.0, 7.0)
    print(result)