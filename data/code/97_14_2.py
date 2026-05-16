def generate_xor_truth_table(a_values, b_values):
    results = []
    for a in a_values:
        for b in b_values:
            xor_result = a ^ b
            results.append((a, b, xor_result))
    return results
if __name__ == '__main__':
    a_inputs = [0, 1]
    b_inputs = [0, 1]
    truth_table = generate_xor_truth_table(a_inputs, b_inputs)
    print("Binary Input A | Binary Input B | XOR Result")
    print("------------------------------------")
    for a, b, xor_result in truth_table:
        print(f"{a}         | {b}         | {xor_result}")