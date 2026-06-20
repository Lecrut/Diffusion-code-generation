import itertools

def generate_truth_table(operators):
    for operator in operators:
        print(f"Truth table for {operator}:")
        if operator == 'AND':
            truth_values = list(itertools.product([False, True], repeat=2))
            results = [x and y for x, y in truth_values]
        elif operator == 'OR':
            truth_values = list(itertools.product([False, True], repeat=2))
            results = [x or y for x, y in truth_values]
        elif operator == 'NOT':
            truth_values = list(itertools.product([False, True]))
            results = [not x for x in truth_values]
        elif operator == 'XOR':
            truth_values = list(itertools.product([False, True], repeat=2))
            results = [x != y for x, y in truth_values]
        elif operator == 'NOR':
            truth_values = list(itertools.product([False, True], repeat=2))
            results = [not (x or y) for x, y in truth_values]
        elif operator == 'NAND':
            truth_values = list(itertools.product([False, True], repeat=2))
            results = [not (x and y) for x, y in truth_values]
        
        print(f"Inputs: {truth_values}")
        print(f"Outputs: {results}\n")

if __name__ == '__main__':
    operators = ['AND', 'OR', 'NOT', 'XOR', 'NOR', 'NAND']
    generate_truth_table(operators)