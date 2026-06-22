def evaluate_expression(inputs):
    results = []
    for input_set in inputs:
        values = dict(input_set)
        A = values.get('A', False)
        B = values.get('B', False)
        C = values.get('C', False)
        D = values.get('D', False)
        result = (A and B) or (C and not D)
        results.append(result)
    return results

if __name__ == '__main__':
    sample_inputs = [
        [('A', True), ('B', False), ('C', True), ('D', False)],
        [('A', False), ('B', True), ('C', False), ('D', True)],
        [('A', True), ('B', True), ('C', False), ('D', True)],
        [('A', False), ('B', False), ('C', True), ('D', True)],
    ]
    print(evaluate_expression(sample_inputs))