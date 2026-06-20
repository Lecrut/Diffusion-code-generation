class LogicalOperations:
    @staticmethod
    def check_both_true(val1: bool, val2: bool) -> bool:
        return val1 and val2

if __name__ == '__main__':
    logical_ops = LogicalOperations()
    print(logical_ops.check_both_true(True, True))
    print(logical_ops.check_both_true(True, False))
    print(logical_ops.check_both_true(False, True))
    print(logical_ops.check_both_true(False, False))