def generate_truth_table(gate):
    inputs = [(x, y) for x in [False, True] for y in [False, True]]
    results = {inputs[i]: gate(inputs[i][0], inputs[i][1]) for i in range(len(inputs))}
    return results

and_gate = lambda x, y: x and y
or_gate = lambda x, y: x or y
not_gate = lambda x: not x

if __name__ == '__main__':
    print("AND Gate Truth Table:")
    print(generate_truth_table(and_gate))
    
    print("\nOR Gate Truth Table:")
    print(generate_truth_table(or_gate))
    
    print("\nNOT Gate Truth Table:")
    print(generate_truth_table(not_gate))