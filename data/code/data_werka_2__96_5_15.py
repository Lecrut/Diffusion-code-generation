class BooleanExpressionEvaluator:
    EXPRESSION_TEMPLATE = (
        "({0} and {1}) or ({2} and not {3})"
    )
    REQUIRED_VARS = ('A', 'B', 'C', 'D')

    @staticmethod
    def _validate_input(input_set):
        var_dict = dict(input_set)
        missing = [v for v in BooleanExpressionEvaluator.REQUIRED_VARS if v not in var_dict]
        if missing:
            raise ValueError(f"Missing variables: {missing}")
        return var_dict

    @staticmethod
    def evaluate_expression(input_list):
        results = []
        for input_set in input_list:
            var_dict = BooleanExpressionEvaluator._validate_input(input_set)
            A = var_dict['A']
            B = var_dict['B']
            C = var_dict['C']
            D = var_dict['D']
            term1 = A and B
            term2 = C and (not D)
            result = term1 or term2
            results.append(result)
        return results

if __name__ == '__main__':
    sample_data = [
        [('A', True), ('B', True), ('C', False), ('D', False)],
        [('A', False), ('B', False), ('C', True), ('D', True)],
        [('A', True), ('B', False), ('C', True), ('D', False)],
        [('A', False), ('B', True), ('C', False), ('D', True)],
    ]
    evaluator = BooleanExpressionEvaluator()
    output = evaluator.evaluate_expression(sample_data)
    print(output)