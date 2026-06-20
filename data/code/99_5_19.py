class ExpressionCalculator:
    OPERATORS = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else float('inf')
    }

    @staticmethod
    def calculate_expression(operands, operators):
        result = operands[0]
        for operator in operators:
            if operator not in ExpressionCalculator.OPERATORS:
                raise ValueError(f"Unsupported operator: {operator}")
            result = ExpressionCalculator.OPERATORS[operator](result, operands[operators.index(operator) + 1])
        return result

if __name__ == '__main__':
    calculator = ExpressionCalculator()
    print(calculator.calculate_expression([2, 3, 4, 5], ['+', '*', '-']))