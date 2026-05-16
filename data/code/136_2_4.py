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
    results = []
    results.append(a and b)
    results.append(a or b)
    results.append(a ^ b)
    results.append(not a)
    results.append(not b)
    results.append(not (a and b))
    results.append(not (a or b))
    results.append(not (a ^ b))
    ops = ['and', 'or', 'xor', 'not']
    final_results = []
    final_results.append(a and b)
    final_results.append(a or b)
    final_results.append(a ^ b)
    final_results.append(not a)
    final_results.append(not b)
    final_results.append(not (a and b))
    final_results.append(not (a or b))
    final_results.append(not (a ^ b))
    return final_results
if __name__ == '__main__':
    a_val = True
    b_val = False
    results = evaluate_boolean_expressions(a_val, b_val)
    for res in results:
        print(res)