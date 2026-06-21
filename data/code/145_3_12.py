class BooleanEvaluator:
    AND = 1
    OR = 2
    NOT = 3

    @staticmethod
    def evaluate(expression):
        tokens = expression.split()
        result_stack = []
        operator_stack = []

        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                operand_stack.append(int(token))
            elif token == 'AND':
                operator_stack.append(BooleanEvaluator.AND)
            elif token == 'OR':
                operator_stack.append(BooleanEvaluator.OR)
            elif token == 'NOT':
                operator_stack.append(BooleanEvaluator.NOT)

        while operator_stack:
            op = operator_stack.pop()
            if op == BooleanEvaluator.NOT:
                operand = operand_stack.pop()
                result_stack.append(1 - operand)
            else:
                b = operand_stack.pop()
                a = operand_stack.pop()
                if op == BooleanEvaluator.AND:
                    result_stack.append(a & b)
                elif op == BooleanEvaluator.OR:
                    result_stack.append(a | b)

        return result_stack[0]

if __name__ == '__main__':
    expression = "1 AND 0 OR 1"
    print(BooleanEvaluator.evaluate(expression))