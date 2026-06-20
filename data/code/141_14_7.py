def generate_truth_table(logic_function):
    inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    return {inputs[i]: logic_function(*inputs[i]) for i in range(len(inputs))}

def and_gate(a, b):
    return a & b

def or_gate(a, b):
    return a | b

def not_gate(a):
    return ~a

if __name__ == '__main__':
    print("AND Gate Truth Table:")
    and_table = generate_truth_table(and_gate)
    for input_pair, result in and_table.items():
        print(f"A: {input_pair[0]} ({bin(input_pair[0])}), B: {input_pair[1]} ({bin(input_pair[1])}) -> Result: {result} ({bin(result)})")

    print("\nOR Gate Truth Table:")
    or_table = generate_truth_table(or_gate)
    for input_pair, result in or_table.items():
        print(f"A: {input_pair[0]} ({bin(input_pair[0])}), B: {input_pair[1]} ({bin(input_pair[1])}) -> Result: {result} ({bin(result)})")

    print("\nNOT Gate Truth Table:")
    not_table = generate_truth_table(not_gate)
    for input_value, result in not_table.items():
        print(f"A: {input_value[0]} ({bin(input_value[0])}) -> Result: {result} ({bin(result)})")