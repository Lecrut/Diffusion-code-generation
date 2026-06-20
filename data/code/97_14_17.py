def generate_or_truth_table(a_values, b_values):
    results = []
    for a in a_values:
        for b in b_values:
            or_result = a or b
            results.append({'a': a, 'b': b, 'or_result': or_result})
    return results

if __name__ == '__main__':
    a_inputs = [True, False]
    b_inputs = [True, False]
    truth_table = generate_or_truth_table(a_inputs, b_inputs)
    print("A | B | A OR B")
    print("---|---|--------")
    for row in truth_table:
        print(f"{row['a']} | {row['b']} | {row['or_result']}")