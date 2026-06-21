class ExpressionEvaluator:
    EXPRESSION_TEMPLATE = "(A and B) or (C and not D)"
    
    @staticmethod
    def _get_bool(variables, name):
        return variables.get(name, False)

    def evaluate_batch(self, input_list):
        results = []
        for variable_set in input_list:
            mapping = dict(variable_set)
            A = self._get_bool(mapping, 'A')
            B = self._get_bool(mapping, 'B')
            C = self._get_bool(mapping, 'C')
            D = self._get_bool(mapping, 'D')
            
            left_side = A and B
            right_side = C and (not D)
            final_value = left_side or right_side
            results.append(final_value)
        return results

if __name__ == '__main__':
    evaluator = ExpressionEvaluator()
    test_data = [
        [('A', True), ('B', True), ('C', False), ('D', False)],
        [('A', False), ('B', False), ('C', True), ('D', True)],
        [('A', True), ('B', False), ('C', True), ('D', False)],
        [('A', False), ('B', True), ('C', False), ('D', True)],
    ]
    output = evaluator.evaluate_batch(test_data)
    print(output)