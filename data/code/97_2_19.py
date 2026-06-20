def generate_truth_table(inputs):
    results = []
    for values in inputs:
        result = tuple(values)
        results.append(result)
    return results

def display_truth_table(results):
    print("A | B | C | A AND B | A AND C | B AND C | A AND B AND C")
    print("-" * 60)
    for a, b, c in results:
        ab = a & b
        ac = a & c
        bc = b & c
        abc = a & b & c
        print(f"{a} | {b} | {c} | {ab} | {ac} | {bc} | {abc}")

if __name__ == '__main__':
    sample_inputs = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
                      (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
    table_results = generate_truth_table(sample_inputs)
    display_truth_table(table_results)