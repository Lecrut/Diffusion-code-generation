class LogicalConjunction:
    @staticmethod
    def short_circuit_and(a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    evaluator = LogicalConjunction()
    print(evaluator.short_circuit_and(True, False))
    print(evaluator.short_circuit_and(False, True))
    print(evaluator.short_circuit_and(True, True))
    print(evaluator.short_circuit_and(False, False))