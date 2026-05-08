def generate_truth_table(booleans, operation):
    n = len(booleans)
    results = []
    for i in range(2**n):
        current_combination = []
        temp = i
        for _ in range(n):
            current_combination.append(temp % 2)
            temp //= 2
        bool_list = [bool(x) for x in current_combination[::-1]]
        if not bool_list:
            continue
        result = None
        if operation == "AND":
            result = all(bool_list)
        elif operation == "OR":
            result = any(bool_list)
        else:
            raise ValueError("Unsupported operation")
        results.append(tuple(bool_list) + (result,))
    return results
if __name__ == '__main__':
    input_booleans = [False, True]
    operation_type = "AND"
    truth_table = generate_truth_table(input_booleans, operation_type)
    print(f"Truth Table for {operation_type} on inputs {input_booleans}:")
    header = "Input 1 | Input 2 | Result"
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    for row in truth_table:
        input1, input2, result = row
        print(f"{input1} | {input2} | {result}")