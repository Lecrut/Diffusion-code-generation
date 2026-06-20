class LogicalOperations:
    @staticmethod
    def check_or_condition(a: bool, b: bool) -> bool:
        return a or b

if __name__ == '__main__':
    print(LogicalOperations.check_or_condition(True, False))
    print(LogicalOperations.check_or_condition(False, True))
    print(LogicalOperations.check_or_condition(True, True))
    print(LogicalOperations.check_or_condition(False, False))