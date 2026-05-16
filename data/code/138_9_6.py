def generate_truth_table(inputs, operation):
    results = []
    n = len(inputs)
    for i in range(2**n):
        current_inputs = []
        temp = i
        for _ in range(n):
            current_inputs.append(temp % 2)
            temp //= 2
        current_inputs.reverse()
        if len(current_inputs) != n:
            continue
        result = None
        if operation == "AND":
            result = all(current_inputs)
        elif operation == "OR":
            result = any(current_inputs)
        elif operation == "XOR":
            result = current_inputs[0] ^ current_inputs[1] if n == 2 else False
            if n > 2:
                result = False
        elif operation == "NOT":
            result = not current_inputs[0]
        else:
            result = "Unknown Operation"
        results.append(tuple(current_inputs) + (result,))
    header = ["Input 1", "Input 2", "Input 3", "Output"]
    table = [header]
    for row in results:
        table.append(list(row))
    return table
if __name__ == '__main__':
    boolean_list = [False, True]
    operation_name = "AND"
    truth_table = generate_truth_table(boolean_list, operation_name)
    print(f"Truth Table for {operation_name}:")
    for row in truth_table:
        print(row)
    boolean_list_2 = [False, False, True, True]
    operation_name_2 = "OR"
    truth_table_2 = generate_truth_table(boolean_list_2, operation_name_2)
    print(f"\nTruth Table for {operation_name_2}:")
    for row in truth_table_2:
        print(row)
    boolean_list_3 = [True]
    operation_name_3 = "NOT"
    truth_table_3 = generate_truth_table(boolean_list_3, operation_name_3)
    print(f"\nTruth Table for {operation_name_3}:")
    for row in truth_table_3:
        print(row)