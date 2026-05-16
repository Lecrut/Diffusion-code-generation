def simulate_logic_gates():
    inputs = [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1)
    ]
    results = {}
    for a, b in inputs:
        and_result = a & b
        or_result = a | b
        not_a_result = 1 - a
        not_b_result = 1 - b
        results[(a, b)] = {
            "AND": and_result,
            "OR": or_result,
            "NOT_A": not_a_result,
            "NOT_B": not_b_result
        }
    for (a, b), res in results.items():
        print(f"Inputs: A={a}, B={b}")
        print(f"AND: {res['AND']}")
        print(f"OR: {res['OR']}")
        print(f"NOT A: {res['NOT_A']}")
        print(f"NOT B: {res['NOT_B']}")
        print("-" * 10)
if __name__ == '__main__':
    simulate_logic_gates()