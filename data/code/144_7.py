def solve_truth_table(variables):
    n = len(variables)
    results = []
    for i in range(2**n):
        row = []
        for j in range(n):
            bit = (i >> j) & 1
            row.append(str(bit))
        results.append(row)
    return results
if __name__ == '__main__':
    variables = ["A", "B"]
    all_combinations = solve_truth_table(variables)
    print("Truth Table for A and B:")
    header = "A | B"
    print(header)
    print("-" * len(header))
    for combination in all_combinations:
        print(f"{combination[0]} | {combination[1]}")