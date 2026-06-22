class ExpressionEvaluator:
    OPERATIONS = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }
    PRECEDENCE = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    @staticmethod
    def get_precedence(operator):
        return ExpressionEvaluator.PRECEDENCE.get(operator, 0)

    @staticmethod
    def perform_operation(left, right, operator):
        if operator == '/':
            if right == 0:
                raise ValueError("Division by zero is not allowed.")
        return ExpressionEvaluator.OPERATIONS[operator](left, right)

    @staticmethod
    def calculate(operands, operators):
        if len(operands) != len(operators) + 1:
            raise ValueError('Operands and operators must form a valid expression sequence.')
        if not operands:
            return 0
        
        values = [operands[0]]
        ops = []

        for i, current_op in enumerate(operators):
            right_operand = operands[i + 1]
            
            while (ops and 
                   ExpressionEvaluator.get_precedence(ops[-1]) >= 
                   ExpressionEvaluator.get_precedence(current_op)):
                op = ops.pop()
                val2 = values.pop()
                val1 = values.pop()
                result = ExpressionEvaluator.perform_operation(val1, val2, op)
                values.append(result)
            
            values.append(right_operand)
            ops.append(current_op)

        while ops:
            op = ops.pop()
            val2 = values.pop()
            val1 = values.pop()
            result = ExpressionEvaluator.perform_operation(val1, val2, op)
            values.append(result)

        return values[0]

if __name__ == '__main__':
    op_list = [2, 3, 5, 7, 1]
    operator_list = ['+', '*', '-', '/']
    result = ExpressionEvaluator.calculate(op_list, operator_list)
    print(result)