class LogicEvaluator:
    @staticmethod
    def short_circuit_and(a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    result = LogicEvaluator.short_circuit_and(True, False)
    print(result)