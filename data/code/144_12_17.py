from itertools import product
VARIABLES = ('A', 'B', 'C')
FORMULA_PARTS = [('AND', ['A', 'B']), ('NOT', ['C'])]

def evaluate_formula(A, B, C):
    part1 = A and B
    part2 = not C
    return part1 or part2

def generate_truth_table(variables, formula_parts):
    truth_table = []
    for combination in product([True, False], repeat=len(variables)):
        row_values = {var: val for var, val in zip(variables, combination)}
        result = evaluate_formula(**row_values)
        truth_table.append(combination + (result,))
    return truth_table
if __name__ == '__main__':
    truth_table = generate_truth_table(VARIABLES, FORMULA_PARTS)
    print(truth_table)