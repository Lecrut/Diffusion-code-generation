class BooleanChecker:
    @staticmethod
    def are_both_true(value1: bool, value2: bool) -> str:
        if value1 and value2:
            return "Both values are True"
        else:
            return "At least one value is False"

if __name__ == '__main__':
    result = BooleanChecker.are_both_true(True, True)
    print(result)