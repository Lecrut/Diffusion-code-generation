class LogicEvaluator:
    @staticmethod
    def validate_inputs(a: bool, b: bool) -> None:
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError("Inputs must be boolean values")

    @staticmethod
    def evaluate_and(a: bool, b: bool) -> bool:
        LogicEvaluator.validate_inputs(a, b)
        return a and b

if __name__ == '__main__':
    result = LogicEvaluator.evaluate_and(True, False)
    print(result)