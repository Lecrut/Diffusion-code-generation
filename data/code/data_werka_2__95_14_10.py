class ConditionChecker:
    THRESHOLD = 0.0

    @staticmethod
    def validate(first: float, second: float, third: float) -> bool:
        return first > ConditionChecker.THRESHOLD and second < first and third == first + second

if __name__ == '__main__':
    checker = ConditionChecker()
    result = checker.validate(10.0, 5.0, 15.0)
    print(result)