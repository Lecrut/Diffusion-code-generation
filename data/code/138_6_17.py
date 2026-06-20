def evaluate_truth_table():
    def generate_combinations(n):
        return [(i >> j) & 1 for j in range(n)]

    def calculate_implication(A, B):
        return not A or B

    def calculate_equivalence(A, B):
        return A == B

    variables = ['A', 'B']
    n = len(variables)
    combinations = generate_combinations(n)

    results = []
    for combination in combinations:
        inputs = {variables[i]: bool(combination) for i in range(n)}
        implication_result = calculate_implication(inputs['A'], inputs['B'])
        equivalence_result = calculate_equivalence(inputs['A'], inputs['B'])
        results.append((inputs, implication_result, equivalence_result))

    return results

if __name__ == '__main__':
    truth_table = evaluate_truth_table()
    for row in truth_table:
        print(row)