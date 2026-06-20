import itertools

def generate_truth_table(operator):
    truth_values = list(itertools.product([False, True], repeat=2))
    results = [operator(a, b) for a, b in truth_values]
    return truth_values, results

def and_operator(a, b):
    return a and b

def or_operator(a, b):
    return a or b

def not_operator(a):
    return not a

def xor_operator(a, b):
    return a != b

def nor_operator(a, b):
    return not (a or b)

def nand_operator(a, b):
    return not (a and b)

if __name__ == '__main__':
    operators = {
        'AND': and_operator,
        'OR': or_operator,
        'NOT': not_operator,
        'XOR': xor_operator,
        'NOR': nor_operator,
        'NAND': nand_operator
    }

    for operator_name, operator in operators.items():
        truth_values, results = generate_truth_table(operator)
        print(f"{operator_name} Truth Table:")
        for i, (a, b) in enumerate(truth_values):
            print(f"A: {a}, B: {b}, Result: {results[i]}")