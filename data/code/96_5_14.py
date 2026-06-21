def evaluate_expression(input_list):
    results = []
    for record in input_list:
        mapping = dict(record)
        a = mapping.get('A', False)
        b = mapping.get('B', False)
        c = mapping.get('C', False)
        d = mapping.get('D', False)
        first_part = a and b
        if first_part:
            results.append(True)
            continue
        second_part = c and not d
        results.append(second_part)
    return results

if __name__ == '__main__':
    test_data = [
        [('A', True), ('B', True), ('C', False), ('D', False)],
        [('A', False), ('B', False), ('C', True), ('D', True)],
        [('A', True), ('B', False), ('C', True), ('D', False)],
        [('A', False), ('B', True), ('C', False), ('D', True)],
    ]
    output = evaluate_expression(test_data)
    print(output)