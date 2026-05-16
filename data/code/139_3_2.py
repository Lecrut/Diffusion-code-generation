def simulate_logic_gates(a, b):
    and_result = a & b
    or_result = a | b
    not_a_result = not a
    not_b_result = not b
    return {
        "AND": and_result,
        "OR": or_result,
        "NOT_A": not_a_result,
        "NOT_B": not_b_result
    }
if __name__ == '__main__':
    inputs = [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1)
    ]
    for a, b in inputs:
        results = simulate_logic_gates(a, b)
        print(f"Inputs: a={a}, b={b}")
        print(f"AND: {results['AND']}")
        print(f"OR: {results['OR']}")
        print(f"NOT A: {results['NOT_A']}")
        print(f"NOT B: {results['NOT_B']}")
        print("-" * 10)