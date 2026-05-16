def generate_truth_table(inputs, operation):
    results = []
    n = len(inputs)
    for i in range(2**n):
        if i == 0:
            a = False
            b = False
        else:
            a = True
            b = False
            temp = i
            while temp > 0:
                if temp & 1:
                    a = not a
                temp >>= 1
                if temp > 0:
                    b = not b
                temp >>= 1
        if operation == 'and':
            result = a and b
        elif operation == 'or':
            result = a or b
        elif operation == 'xor':
            result = a ^ b
        elif operation == 'not':
            result = not a
        else:
            raise ValueError("Unsupported operation")
        results.append((a, b, result))
    return results
if __name__ == '__main__':
    boolean_inputs = [False, True]
    operation_type = 'and'
    truth_table = generate_truth_table(boolean_inputs, operation_type)
    print(f"Truth Table for {operation_type}:")
    for a, b, result in truth_table:
        print(f"A: {a}, B: {b} -> Result: {result}")
    boolean_inputs_2 = [True, False]
    operation_type_2 = 'xor'
    truth_table_2 = generate_truth_table(boolean_inputs_2, operation_type_2)
    print(f"\nTruth Table for {operation_type_2}:")
    for a, b, result in truth_table_2:
        print(f"A: {a}, B: {b} -> Result: {result}")
    boolean_inputs_3 = [True]
    operation_type_3 = 'not'
    truth_table_3 = generate_truth_table(boolean_inputs_3, operation_type_3)
    print(f"\nTruth Table for {operation_type_3}:")
    for a, b, result in truth_table_3:
        print(f"A: {a} -> Result: {result}")