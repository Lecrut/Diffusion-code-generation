def evaluate_boolean_expressions(a, b):
    results = []
    results.append(a and b)
    results.append(a or b)
    results.append(a ^ b)
    results.append(not a)
    results.append(not b)
    inputs = [a, not a, b, not b]
    for i in range(4):
        for j in range(4):
            val1 = inputs[i]
            val2 = inputs[j]
            results.append(val1 and val2)
            results.append(val1 or val2)
            results.append(val1 ^ val2)
            results.append(not val1)
            results.append(not val2)
    unique_results = set(results)
    final_list = sorted(list(unique_results))
    for res in final_list:
        print(res)
if __name__ == '__main__':
    a_val = True
    b_val = False
    evaluate_boolean_expressions(a_val, b_val)