def generate_truth_table(inputs, operation):
    results = []
    n = len(inputs)
    for i in range(2**n):
        row = []
        temp = i
        for _ in range(n):
            row.append(bool(temp % 2))
            temp //= 2
        result = None
        if operation == 'and':
            result = all(row)
        elif operation == 'or':
            result = any(row)
        elif operation == 'xor':
            result = (sum(row) % 2) == 1
        elif operation == 'not':
            result = not row[0]
        else:
            result = "Unknown Operation"
        results.append(row + [result])
    return results
if __name__ == '__main__':
    boolean_inputs = [False, True]
    print("--- AND Operation ---")
    and_table = generate_truth_table(boolean_inputs, 'and')
    for row in and_table:
        print(row)
    print("\n--- OR Operation ---")
    or_table = generate_truth_table(boolean_inputs, 'or')
    for row in or_table:
        print(row)
    print("\n--- XOR Operation ---")
    xor_table = generate_truth_table(boolean_inputs, 'xor')
    for row in xor_table:
        print(row)
    print("\n--- NOT Operation (applied to the first input) ---")
    not_table = generate_truth_table(boolean_inputs, 'not')
    for row in not_table:
        print(row)