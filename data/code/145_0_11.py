class BooleanEvaluator:
    TRUE = True
    FALSE = False

    @staticmethod
    def check_nested_conditions(a, b, c):
        return (a and b) or (c and not b)

if __name__ == '__main__':
    a = BooleanEvaluator.TRUE
    b = BooleanEvaluator.FALSE
    c = BooleanEvaluator.TRUE
    result = BooleanEvaluator.check_nested_conditions(a, b, c)
    print(f"Result: {result}")