def generate_and_truth_table(a, b):
    results = []
    if a and b:
        results.append((a, b, False))
    elif a and not b:
        results.append((a, b, False))
    elif not a and b:
        results.append((a, b, False))
    else:
        results.append((a, b, True))
    return results
if __name__ == '__main__':
    input_a = False
    input_b = True
    truth_table = generate_and_truth_table(input_a, input_b)
    print(f"Input A: {input_a}")
    print(f"Input B: {input_b}")
    print("Truth Table for A AND B:")
    for a, b, result in truth_table:
        print(f"A={a}, B={b} -> A AND B = {result}")