def generate_truth_table(operation):
    truth_table = {
        'AND': [(True, True), (True, False), (False, True), (False, False)],
        'OR': [(True, True), (True, False), (False, True), (False, False)],
        'XOR': [(True, True), (True, False), (False, True), (False, False)]
    }
    
    results = []
    for a, b in truth_table[operation]:
        if operation == 'AND':
            result = a and b
        elif operation == 'OR':
            result = a or b
        else:
            result = a != b
        results.append((a, b, result))
    
    return results

if __name__ == '__main__':
    operations = ['AND', 'OR', 'XOR']
    for op in operations:
        print(f"Truth Table for {op}:")
        table = generate_truth_table(op)
        for a, b, result in table:
            print(f"A: {a}, B: {b}, {op}: {result}")