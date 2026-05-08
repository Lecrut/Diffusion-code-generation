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
            result = row[0]
            for j in range(1, n):
                result = result ^ row[j]
        elif operation == 'not_all':
            result = not all(row)
        else:
            raise ValueError("Unsupported operation")
        results.append(row + [result])
    return results
if __name__ == '__main__':
    boolean_inputs = [False, True]
    print("--- AND Truth Table ---")
    and_table = generate_truth_table(boolean_inputs, 'and')
    for row in and_table:
        print(row)
    print("\n--- OR Truth Table ---")
    or_table = generate_truth_table(boolean_inputs, 'or')
    for row in or_table:
        print(row)
    print("\n--- XOR Truth Table ---")
    xor_table = generate_truth_table(boolean_inputs, 'xor')
    for row in xor_table:
        print(row)
    print("\n--- NOT_ALL Truth Table ---")
    not_all_table = generate_truth_table(boolean_inputs, 'not_all')
    for row in not_all_table:
        print(row)