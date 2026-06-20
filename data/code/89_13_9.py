class BooleanEvaluator:
    @staticmethod
    def is_valid_boolean(value):
        if not isinstance(value, bool):
            raise ValueError("Both arguments must be boolean values.")
    
    @staticmethod
    def evaluate_and(a: bool, b: bool) -> bool:
        BooleanEvaluator.is_valid_boolean(a)
        BooleanEvaluator.is_valid_boolean(b)
        return a and b

if __name__ == '__main__':
    result = BooleanEvaluator.evaluate_and(True, False)
    print(result)