def evaluate_boolean_expressions(a, b):
    results = []
    results.append(a and b)
    results.append(a or b)
    results.append(a ^ b)
    results.append(not a)
    results.append(not b)
    results.append(not (a and b))
    results.append(not (a or b))
    results.append(not (a ^ b))
    results.append(a and (not b))
    results.append((not a) and b)
    results.append(a or (not b))
    results.append((not a) or b)
    final_results = [
        a and b,
        a or b,
        a ^ b,
        not a,
        not b,
        not (a and b),
        not (a or b),
        not (a ^ b)
    ]
    return final_results
if __name__ == '__main__':
    a_val = True
    b_val = False
    results = evaluate_boolean_expressions(a_val, b_val)
    print(f"Input A: {a_val}")
    print(f"Input B: {b_val}")
    print("Results of logical combinations:")
    for res in results:
        print(res)