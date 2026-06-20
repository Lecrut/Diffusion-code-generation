def generate_truth_table(logical_operation):
    results = []
    for a in [True, False]:
        for b in [True, False]:
            if logical_operation == 'AND':
                result = a and b
            elif logical_operation == 'OR':
                result = a or b
            elif logical_operation == 'XOR':
                result = a != b
            results.append((a, b, result))
    return results

if __name__ == '__main__':
    logical_operations = ['AND', 'OR', 'XOR']
    for operation in logical_operations:
        print(f"Truth Table for {operation}:")
        truth_table = generate_truth_table(operation)
        for a, b, result in truth_table:
            print(f"A: {a}, B: {b}, {operation}: {result}")