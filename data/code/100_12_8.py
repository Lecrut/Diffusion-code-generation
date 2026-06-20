class LogicalEvaluator:
    OPERATORS = {
        'AND': all,
        'OR': any
    }

    @staticmethod
    def evaluate(statement, variables):
        parts = statement.split()
        if len(parts) != 3:
            raise ValueError("Invalid statement format")
        
        left, operator, right = parts
        if operator not in LogicalEvaluator.OPERATORS:
            raise ValueError("Unsupported operator")
        
        return LogicalEvaluator.OPERATORS[operator]([variables[left], variables[right]])

if __name__ == '__main__':
    evaluator = LogicalEvaluator()
    sample_statement = 'A AND B'
    sample_variables = {'A': True, 'B': False}
    result = evaluator.evaluate(sample_statement, sample_variables)
    print(result)