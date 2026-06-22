class ExpressionEvaluator:
    OPERATOR_PRECEDENCE = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    @staticmethod
    def _apply_operator(left, operator, right):
        if operator == '+':
            return left + right
        if operator == '-':
            return left - right
        if operator == '*':
            return left * right
        if operator == '/':
            if right == 0:
                raise ValueError('Division by zero is not allowed.')
            return left / right
        raise ValueError(f'Unsupported operator: {operator}')

    @classmethod
    def evaluate(cls, operands, operators):
        if len(operands) != len(operators) + 1:
            raise ValueError('Operands and operators must form a valid expression sequence.')
        if not operands:
            return 0

        values = [operands[0]]
        ops = []

        for i, op in enumerate(operators):
            current_operand = operands[i + 1]
            
            while (ops and 
                   cls.OPERATOR_PRECEDENCE.get(ops[-1], 0) >= cls.OPERATOR_PRECEDENCE.get(op, 0)):
                prev_op = ops.pop()
                right_val = values.pop()
                left_val = values.pop()
                result = cls._apply_operator(left_val, prev_op, right_val)
                values.append(result)
            
            ops.append(op)
            values.append(current_operand)

        while ops:
            prev_op = ops.pop()
            right_val = values.pop()
            left_val = values.pop()
            result = cls._apply_operator(left_val, prev_op, right_val)
            values.append(result)

        return values[0]

if __name__ == '__main__':
    operands = [3, 5, 2, 8, 1]
    operators = ['+', '*', '-', '/']
    result = ExpressionEvaluator.evaluate(operands, operators)
    print(result)