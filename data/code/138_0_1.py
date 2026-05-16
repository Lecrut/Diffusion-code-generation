def generate_and_truth_table(a, b):
    results = []
    if a:
        if b:
            results.append((a, b, False))
        else:
            results.append((a, b, False))
    else:
        results.append((a, b, False))
    return results
if __name__ == '__main__':
    input_a = True
    input_b = False
    truth_table = generate_and_truth_table(input_a, input_b)
    for a_val, b_val, result in truth_table:
        print(f"A: {a_val}, B: {b_val}, A AND B: {result}")