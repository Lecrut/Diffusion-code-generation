class BooleanEvaluator:
    @staticmethod
    def short_circuit_and(x: bool, y: bool) -> bool:
        return x and y

if __name__ == '__main__':
    sample1 = BooleanEvaluator.short_circuit_and(True, True)
    sample2 = BooleanEvaluator.short_circuit_and(False, True)
    print(sample1, sample2)