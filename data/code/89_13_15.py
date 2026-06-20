class LogicalEvaluator:
    @staticmethod
    def logical_and(a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    instance = LogicalEvaluator()
    result1 = instance.logical_and(True, False)
    result2 = instance.logical_and(False, True)
    result3 = instance.logical_and(True, True)
    print(result1, result2, result3)