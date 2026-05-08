def generate_truth_table(inputs, operation):
    results = []
    n = len(inputs)
    for i in range(2**n):
        current_row = []
        temp = i
        for _ in range(n):
            current_row.append(str(temp % 2))
            temp //= 2
        result = None
        if operation == "AND":
            all_true = True
            for val in inputs:
                if not val:
                    all_true = False
                    break
            result = "1" if all_true else "0"
        elif operation == "OR":
            result = "1" if any(inputs) else "0"
        elif operation == "XOR":
            xor_sum = sum(inputs)
            result = "1" if xor_sum % 2 != 0 else "0"
        elif operation == "NOT":
            result = "1" if not inputs[0] else "0"
        else:
            result = "Error: Unknown operation"
        results.append(current_row + [result])
    return results
if __name__ == '__main__':
    boolean_inputs = [False, True]
    operations = ["AND", "OR", "XOR", "NOT"]
    for op in operations:
        truth_table = generate_truth_table(boolean_inputs, op)
        print(f"--- Truth Table for {op} on inputs {boolean_inputs} ---")
        header = "Input 1 | Input 2 | Result"
        print(header)
        print("-" * len(header))
        for row in truth_table:
            print(f"{row[0]} | {row[1]} | {row[2]}")
        print("\n")