class BooleanExpressionEvaluator:
    EXPRESSION_PATTERN = [('A', 'B', 'C', 'D')]

    @staticmethod
    def _get_value(variables, var_name):
        for name, val in variables:
            if name == var_name:
                return val
        return False

    @staticmethod
    def evaluate_all(input_list):
        results = []
        for variable_set in input_list:
            A = BooleanExpressionEvaluator._get_value(variable_set, 'A')
            B = BooleanExpressionEvaluator._get_value(variable_set, 'B')
            C = BooleanExpressionEvaluator._get_value(variable_set, 'C')
            D = BooleanExpressionEvaluator._get_value(variable_set, 'D')
            
            term1 = A and B
            term2 = C and (not D)
            final_result = term1 or term2
            results.append(final_result)
        return results

if __name__ == '__main__':
    data = [
        [('A', True), ('B', True), ('C', False), ('D', False)],
        [('A', False), ('B', False), ('C', True), ('D', True)],
        [('A', True), ('B', False), ('C', True), ('D', False)],
        [('A', False), ('B', True), ('C', False), ('D', True)],
    ]
    output = BooleanExpressionEvaluator.evaluate_all(data)
    print(output)