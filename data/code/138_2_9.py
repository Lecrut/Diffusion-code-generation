import itertools

def generate_truth_table(operators):
    inputs = list(itertools.product([False, True], repeat=2))
    for operator in operators:
        print(f"\nTruth table for {operator}:")
        if operator == 'AND':
            results = [a and b for a, b in inputs]
        elif operator == 'OR':
            results = [a or b for a, b in inputs]
        elif operator == 'NOT':
            results = [not a for a, b in inputs]
        elif operator == 'XOR':
            results = [a != b for a, b in inputs]
        elif operator == 'NOR':
            results = [not (a or b) for a, b in inputs]
        elif operator == 'NAND':
            results = [not (a and b) for a, b in inputs]
        else:
            continue
        print(f"Inputs: {inputs}")
        print(f"Results: {results}")

if __name__ == '__main__':
    operators = ['AND', 'OR', 'NOT', 'XOR', 'NOR', 'NAND']
    generate_truth_table(operators)