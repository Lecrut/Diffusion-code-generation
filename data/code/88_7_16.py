class BooleanChecker:
    @staticmethod
    def both_true(a: bool, b: bool) -> str:
        if a and b:
            return "Both values are True"
        else:
            return "At least one value is False"

if __name__ == '__main__':
    result = BooleanChecker.both_true(True, True)
    print(result)