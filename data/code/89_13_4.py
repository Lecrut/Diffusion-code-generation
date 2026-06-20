class BoolEvaluator:
    @staticmethod
    def short_circuit_and(a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    result = BoolEvaluator.short_circuit_and(True, False)
    print(result)