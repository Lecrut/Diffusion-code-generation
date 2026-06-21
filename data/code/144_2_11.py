def evaluate_expressions():
    results = []
    for A in [False, True]:
        for B in [False, True]:
            xor_result = (A ^ B)
            and_not_a_b_result = (not A) and B
            if xor_result != and_not_a_b_result:
                raise ValueError(f"Expressions are not logically equivalent for A={A} and B={B}")
            results.append((A, B, xor_result))
    return results

if __name__ == '__main__':
    try:
        evaluation_results = evaluate_expressions()
        print(evaluation_results)
    except ValueError as e:
        print(e)