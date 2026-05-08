def generate_or_truth_table(combinations):
    results = []
    for combo in combinations:
        if len(combo) == 2:
            a, b = combo
            or_result = a or b
            results.append((a, b, or_result))
        else:
            results.append((combo, "Invalid input"))
    return results
if __name__ == '__main__':
    sample_combinations = [
        [True, False],
        [False, True],
        [True, True],
        [False, False]
    ]
    truth_table = generate_or_truth_table(sample_combinations)
    for a, b, result in truth_table:
        print(f"Input: ({a}, {b}) -> OR Result: {result}")