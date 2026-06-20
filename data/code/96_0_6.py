class LogicEvaluator:
    @staticmethod
    def evaluate_nested_logic(a, b, c, d):
        return (a and b) or (c and not d)

if __name__ == '__main__':
    A = True
    B = False
    C = True
    D = False
    result = LogicEvaluator.evaluate_nested_logic(A, B, C, D)
    print(result)