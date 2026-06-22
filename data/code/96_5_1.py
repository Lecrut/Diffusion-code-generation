def evaluate_expression(inputs):
    results = []
    for input_set in inputs:
        variables = dict(input_set)
        A = variables.get('A', False)
        B = variables.get('B', False)
        C = variables.get('C', False)
        D = variables.get('D', False)
        result = (A and B) or (C and not D)
        results.append(result)
    return results

if __name__ == '__main__':
    sample_inputs = [
        [('A', True), ('B', True), ('C', False), ('D', False)],
        [('A', False), ('B', False), ('C', True), ('D', True)],
        [('A', True), ('B', False), ('C', True), ('D', False)],
        [('A', False), ('B', True), ('C', False), ('D', True)],
    ]
    output = evaluate_expression(sample_inputs)
    print(output)