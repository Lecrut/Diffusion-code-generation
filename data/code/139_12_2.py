def simulate_gates(a, b):
    and_result = a & b
    or_result = a | b
    not_a_result = 1 - a
    not_b_result = 1 - b
    not_a_not_b_result = 1 - (a | b)
    return {
        "AND": and_result,
        "OR": or_result,
        "NOT_A": not_a_result,
        "NOT_B": not_b_result,
        "NOT_A_OR_B": not_a_not_b_result
    }
if __name__ == '__main__':
    input_a = 1
    input_b = 0
    results = simulate_gates(input_a, input_b)
    print(f"Input A: {input_a}")
    print(f"Input B: {input_b}")
    print("--- Results ---")
    print(f"AND (A & B): {results['AND']}")
    print(f"OR (A | B): {results['OR']}")
    print(f"NOT A (~A): {results['NOT_A']}")
    print(f"NOT B (~B): {results['NOT_B']}")
    print(f"NOT (A OR B): {results['NOT_A_OR_B']}")