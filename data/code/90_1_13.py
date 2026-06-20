class LogicalOperations:
    @staticmethod
    def check_or_condition(a: bool, b: bool) -> bool:
        return a or b

if __name__ == '__main__':
    logic = LogicalOperations()
    result1 = logic.check_or_condition(True, False)
    print(f"check_or_condition(True, False): {result1}")
    result2 = logic.check_or_condition(False, True)
    print(f"check_or_condition(False, True): {result2}")
    result3 = logic.check_or_condition(True, True)
    print(f"check_or_condition(True, True): {result3}")
    result4 = logic.check_or_condition(False, False)
    print(f"check_or_condition(False, False): {result4}")