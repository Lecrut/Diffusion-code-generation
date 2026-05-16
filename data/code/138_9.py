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
            result = "True" if all_true else "False"
        elif operation == "OR":
            result = "True" if any(inputs) else "False"
        elif operation == "XOR":
            xor_sum = sum(inputs)
            result = "True" if xor_sum % 2 != 0 else "False"
        elif operation == "NOT":
            result = "True" if not inputs[0] else "False"
        else:
            result = "Unknown Operation"
        results.append(current_row + [result])
    return results
if __name__ == '__main__':
    boolean_inputs = [False, True]
    operation_type = "AND"
    truth_table = generate_truth_table(boolean_inputs, operation_type)
    print(f"Inputs: {boolean_inputs}")
    print(f"Operation: {operation_type}")
    print("Truth Table:")
    for row in truth_table:
        print(row)
    boolean_inputs_2 = [False, False, True]
    operation_type_2 = "OR"
    truth_table_2 = generate_truth_table(boolean_inputs_2, operation_type_2)
    print(f"\nInputs: {boolean_inputs_2}")
    print(f"Operation: {operation_type_2}")
    print("Truth Table:")
    for row in truth_table_2:
        print(row)
    boolean_inputs_3 = [True, False]
    operation_type_3 = "XOR"
    truth_table_3 = generate_truth_table(boolean_inputs_3, operation_type_3)
    print(f"\nInputs: {boolean_inputs_3}")
    print(f"Operation: {operation_type_3}")
    print("Truth Table:")
    for row in truth_table_3:
        print(row)