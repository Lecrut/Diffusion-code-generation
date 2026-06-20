class LogicEvaluator:
    @staticmethod
    def validate_inputs(a: bool, b: bool) -> None:
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError("Both inputs must be boolean values")

    @staticmethod
    def short_circuit_and(a: bool, b: bool) -> bool:
        LogicEvaluator.validate_inputs(a, b)
        return a and b

if __name__ == '__main__':
    result = LogicEvaluator.short_circuit_and(True, False)
    print(result)