class LogicEvaluator:
    @staticmethod
    def short_circuit_and(a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    sample1 = LogicEvaluator.short_circuit_and(True, False)
    sample2 = LogicEvaluator.short_circuit_and(False, True)
    print(sample1, sample2)