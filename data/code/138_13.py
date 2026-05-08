def generate_truth_table(booleans, operation):
    n = len(booleans)
    results = []
    for i in range(2**n):
        current_combination = []
        temp = i
        for _ in range(n):
            current_combination.append(bool(temp % 2))
            temp //= 2
        if operation == 'and':
            result = True
            for b in current_combination:
                result = result and b
            results.append((current_combination, result))
        elif operation == 'or':
            result = False
            for b in current_combination:
                result = result or b
            results.append((current_combination, result))
        else:
            raise ValueError("Unsupported operation")
    return results
if __name__ == '__main__':
    input_booleans = [False, True]
    operation_type = 'and'
    truth_table = generate_truth_table(input_booleans, operation_type)
    print(f"Truth Table for {operation_type} operation on input: {input_booleans}")
    print("Input Combinations | Result")
    print("-" * 30)
    for combination, result in truth_table:
        print(f"{list(combination)} | {result}")