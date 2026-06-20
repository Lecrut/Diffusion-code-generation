import itertools

def generate_truth_table(operators):
    inputs = list(itertools.product([False, True], repeat=2))
    for operator in operators:
        print(f"Truth table for {operator}:")
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
            raise ValueError(f"Unsupported operator: {operator}")
        
        print("A | B | Result")
        for i, result in enumerate(results):
            print(f"{inputs[i][0]} | {inputs[i][1]} | {result}")

if __name__ == '__main__':
    operators = ['AND', 'OR', 'NOT', 'XOR', 'NOR', 'NAND']
    generate_truth_table(operators)