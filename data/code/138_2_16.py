import itertools

def generate_truth_table(operator):
    inputs = list(itertools.product([False, True], repeat=2))
    results = [operator(a, b) for a, b in inputs]
    return dict(zip(inputs, results))

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
    print("AND:")
    print(generate_truth_table(and_operator))
    print("\nOR:")
    print(generate_truth_table(or_operator))
    print("\nNOT:")
    for a in [False, True]:
        print(f"not {a}: {not_operator(a)}")
    print("\nXOR:")
    print(generate_truth_table(xor_operator))
    print("\nNOR:")
    print(generate_truth_table(nor_operator))
    print("\nNAND:")
    print(generate_truth_table(nand_operator))