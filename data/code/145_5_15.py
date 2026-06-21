class BooleanEvaluator:
    TRUE = True
    FALSE = False

    @staticmethod
    def apply_de_morgan(expression):
        if expression == BooleanEvaluator.TRUE:
            return BooleanEvaluator.FALSE
        elif expression == BooleanEvaluator.FALSE:
            return BooleanEvaluator.TRUE
        elif isinstance(expression, list) and len(expression) == 2 and expression[0] == "not":
            sub_expression = expression[1]
            if isinstance(sub_expression, list):
                operator, right = sub_expression
                if operator == "and":
                    return ["or", [BooleanEvaluator.apply_de_morgan([BooleanEvaluator.TRUE, right]), BooleanEvaluator.apply_de_morgan([BooleanEvaluator.FALSE, right])]]
                elif operator == "or":
                    return ["and", [BooleanEvaluator.apply_de_morgan([BooleanEvaluator.FALSE, right]), BooleanEvaluator.apply_de_morgan([BooleanEvaluator.TRUE, right])]]
            else:
                raise ValueError("Unsupported sub-expression for not operation")
        elif isinstance(expression, list):
            operator, *operands = expression
            if operator == "and":
                return ["and"] + [BooleanEvaluator.apply_de_morgan(operand) for operand in operands]
            elif operator == "or":
                return ["or"] + [BooleanEvaluator.apply_de_morgan(operand) for operand in operands]
        else:
            raise ValueError("Unsupported expression type")

    @staticmethod
    def flatten_boolean_expression(expression):
        stack = []
        for item in reversed(expression):
            if isinstance(item, list):
                stack.extend(BooleanEvaluator.flatten_boolean_expression(item))
            elif isinstance(item, bool):
                stack.append(item)
            else:
                raise TypeError("Unsupported data type encountered")
        return stack

if __name__ == '__main__':
    nested_structure = [
        "and", [BooleanEvaluator.TRUE, ["not", BooleanEvaluator.FALSE]],
        ["or", [BooleanEvaluator.FALSE, ["not", BooleanEvaluator.TRUE]]]
    ]
    de_morgan_applied = BooleanEvaluator.apply_de_morgan(nested_structure)
    flattened_expression = BooleanEvaluator.flatten_boolean_expression(de_morgan_applied)
    print(f"Flattened Expression: {flattened_expression}")