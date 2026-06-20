def generate_truth_table():
    inputs = [0, 1]
    results_and = [[a & b for b in inputs] for a in inputs]
    results_or = [[a | b for b in inputs] for a in inputs]
    results_not_a = [[~a for b in inputs] for a in inputs]
    results_not_b = [[~b for b in inputs] for a in inputs]
    return results_and, results_or, results_not_a, results_not_b

if __name__ == '__main__':
    and_res, or_res, not_a_res, not_b_res = generate_truth_table()
    print("A AND B:")
    for row in and_res:
        print(row)
    print("\nA OR B:")
    for row in or_res:
        print(row)
    print("\nNOT A:")
    for row in not_a_res:
        print(row)
    print("\nNOT B:")
    for row in not_b_res:
        print(row)