class LogicEvaluator:

    @staticmethod
    def short_circuit_and(a: bool, b: bool) -> bool:
        return a and b
if __name__ == '__main__':
    result1 = LogicEvaluator.short_circuit_and(True, False)
    result2 = LogicEvaluator.short_circuit_and(False, True)
    result3 = LogicEvaluator.short_circuit_and(True, True)
    print(result1)
    print(result2)
    print(result3)