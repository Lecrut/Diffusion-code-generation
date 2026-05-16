def generate_truth_table(booleans, operation):
    n = len(booleans)
    results = []
    for i in range(2**n):
        current_combination = []
        temp = i
        for _ in range(n):
            current_combination.append(temp % 2)
            temp //= 2
        val1 = current_combination[::-1]
        if operation == "and":
            result = all(val1)
        elif operation == "or":
            result = any(val1)
        else:
            raise ValueError("Unsupported operation")
        results.append(tuple(val1) + (result,))
    return results
if __name__ == '__main__':
    input_list = [False, True]
    operation_type = "and"
    truth_table = generate_truth_table(input_list, operation_type)
    print(f"Truth Table for {operation_type} on input {input_list}:")
    header = "Input (A, B) | Result"
    print(header)
    print("-" * len(header))
    for row in truth_table:
        input_str = " ".join(map(str, row[:len(input_list)]))
        result_str = str(row[-1])
        print(f"{input_str} | {result_str}")