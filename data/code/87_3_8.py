class BooleanEvaluator:
    @staticmethod
    def evaluate(condition_a: bool, condition_b: bool, condition_c: bool) -> bool:
        return (condition_a and condition_b) or condition_c

if __name__ == '__main__':
    sample_values = [
        (True, True, False),
        (False, True, True),
        (True, False, True),
        (False, False, False)
    ]
    
    for values in sample_values:
        result = BooleanEvaluator.evaluate(*values)
        print(f"({values[0]}, {values[1]}, {values[2]}) -> {result}")