class LogicEvaluator:
    @staticmethod
    def short_circuit_and(a: bool, b: bool) -> bool:
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError("Both inputs must be boolean values")
        return a and b

if __name__ == '__main__':
    result = LogicEvaluator.short_circuit_and(True, False)
    print(result)