def generate_truth_table(op_name, var1_values, var2_values):
    results = []
    for v1 in var1_values:
        for v2 in var2_values:
            result = False
            if op_name == "AND":
                result = v1 and v2
            elif op_name == "OR":
                result = v1 or v2
            elif op_name == "XOR":
                result = v1 ^ v2
            elif op_name == "NOT_V1":
                result = not v1
            elif op_name == "NOT_V2":
                result = not v2
            else:
                result = "Unknown Operation"
            results.append((v1, v2, result))
    return results
if __name__ == '__main__':
    operation = "AND"
    var1_inputs = [False, True]
    var2_inputs = [False, True]
    truth_table = generate_truth_table(operation, var1_inputs, var2_inputs)
    print(f"Truth Table for {operation} of V1 and V2:")
    print("-" * 30)
    print(f"{'V1':<5} {'V2':<5} {'Result':<6}")
    print("-" * 20)
    for v1, v2, result in truth_table:
        print(f"{str(v1):<5} {str(v2):<5} {str(result):<6}")