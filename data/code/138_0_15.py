def generate_truth_table(operation):
    if operation == 'AND':
        truth_values = [(True, True), (True, False), (False, True), (False, False)]
        results = [(a, b, a and b) for a, b in truth_values]
    elif operation == 'OR':
        truth_values = [(True, True), (True, False), (False, True), (False, False)]
        results = [(a, b, a or b) for a, b in truth_values]
    elif operation == 'XOR':
        truth_values = [(True, True), (True, False), (False, True), (False, False)]
        results = [(a, b, a != b) for a, b in truth_values]
    else:
        raise ValueError("Invalid operation. Supported operations are 'AND', 'OR', and 'XOR'.")
    
    return results

if __name__ == '__main__':
    and_table = generate_truth_table('AND')
    or_table = generate_truth_table('OR')
    xor_table = generate_truth_table('XOR')

    print("Truth Table for AND:")
    for a, b, result in and_table:
        print(f"Input A: {a}, Input B: {b}, Result (A AND B): {result}")

    print("\nTruth Table for OR:")
    for a, b, result in or_table:
        print(f"Input A: {a}, Input B: {b}, Result (A OR B): {result}")

    print("\nTruth Table for XOR:")
    for a, b, result in xor_table:
        print(f"Input A: {a}, Input B: {b}, Result (A XOR B): {result}")