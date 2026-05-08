def generate_and_truth_table(a, b):
    results = []
    if a == False:
        results.append((False, False))
    elif a == True:
        if b == False:
            results.append((False, False))
        elif b == True:
            results.append((True, True))
    return results
if __name__ == '__main__':
    input_a = False
    input_b = True
    truth_table = generate_and_truth_table(input_a, input_b)
    print(f"Input A: {input_a}, Input B: {input_b}")
    print("Truth Table for A AND B:")
    for row in truth_table:
        print(f"A: {row[0]}, B: {row[1]} -> A AND B: {row[0] and row[1]}")