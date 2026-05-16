def generate_truth_table(booleans, operation):
    n = len(booleans)
    rows = 2**n
    truth_table = []
    for i in range(rows):
        input_values = []
        temp = i
        for _ in range(n):
            input_values.append(temp % 2)
            temp //= 2
        result = None
        if operation == "AND":
            result = all(input_values)
        elif operation == "OR":
            result = any(input_values)
        else:
            raise ValueError("Unsupported operation")
        truth_table.append(tuple(input_values) + (result,))
    return truth_table
if __name__ == '__main__':
    input_list = [False, True]
    operation_type = "AND"
    truth_table_result = generate_truth_table(input_list, operation_type)
    print(f"Truth Table for Input: {list(input_list)}")
    print(f"Operation: {operation_type}")
    print("Input values (A, B):")
    header = [f"A", f"B", f"Result ({operation_type})"]
    print(f"{header[0]:<5}{header[1]:<5}{header[2]:<15}")
    print("-" * 35)
    for row in truth_table_result:
        a, b, res = row
        print(f"{a:<5}{b:<5}{res:<15}")