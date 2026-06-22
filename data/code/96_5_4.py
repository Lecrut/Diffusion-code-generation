def evaluate_expression(input_tuples):
    results = []
    for row in input_tuples:
        mapping = dict(row)
        A = mapping.get('A', False)
        B = mapping.get('B', False)
        C = mapping.get('C', False)
        D = mapping.get('D', False)
        term1 = A and B
        if term1:
            results.append(True)
            continue
        term2 = C and not D
        results.append(term2)
    return results

if __name__ == '__main__':
    test_cases = [
        [('A', True), ('B', True), ('C', False), ('D', False)],
        [('A', False), ('B', False), ('C', True), ('D', True)],
        [('A', True), ('B', False), ('C', True), ('D', False)],
        [('A', False), ('B', True), ('C', False), ('D', True)],
    ]
    print(evaluate_expression(test_cases))