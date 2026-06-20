AND_INPUTS = [True, False]

def generate_and_truth_table(combinations):
    results = []
    for combo in combinations:
        if len(combo) == 2:
            a, b = combo
            and_result = a and b
            results.append((a, b, and_result))
        else:
            results.append((None, None, None))
    return results

if __name__ == '__main__':
    sample_combinations = [
        [True, False],
        [False, True],
        [True, True],
        [False, False]
    ]
    truth_table = generate_and_truth_table(sample_combinations)
    for row in truth_table:
        print(f"{row[0]} AND {row[1]} = {row[2]}")