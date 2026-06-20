def evaluate_operations(booleans, operation):
    n = len(booleans)
    results = []
    for i in range(2**n):
        combination = [bool(i & (1 << j)) for j in range(n)]
        if operation == 'and':
            result = all(combination)
        elif operation == 'or':
            result = any(combination)
        else:
            raise ValueError("Unsupported operation")
        results.append((combination, result))
    return results

if __name__ == '__main__':
    booleans = [True, False, True]
    operation = 'and'
    truth_table = evaluate_operations(booleans, operation)
    print(truth_table)