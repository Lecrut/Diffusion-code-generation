class BooleanConditionEvaluator:
    PRECEDENCE_RULES = {
        "and": 2,
        "or": 1
    }

    @staticmethod
    def evaluate_expression(a, b, c, operator_type):
        if operator_type == "and":
            return a and b and c
        if operator_type == "or":
            return a or b or c
        raise ValueError("Unsupported operator type")

    @staticmethod
    def compare_precedence(a, b, c):
        left_associative = (a and b) or c
        right_associative = a and (b or c)
        mixed = a or b and c
        return left_associative, right_associative, mixed

if __name__ == '__main__':
    val_a = True
    val_b = False
    val_c = True
    evaluator = BooleanConditionEvaluator()
    left, right, mixed = evaluator.compare_precedence(val_a, val_b, val_c)
    print(left)
    print(right)
    print(mixed)