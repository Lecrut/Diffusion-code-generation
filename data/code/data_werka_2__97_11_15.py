def generate_or_truth_table(input_combinations):
    results = []
    for combo in input_combinations:
        if len(combo) != 2:
            raise ValueError("Each combination must have exactly two inputs")
        a, b = combo
        results.append([a, b, a or b])
    return results

if __name__ == '__main__':
    inputs = [[True, False], [False, True], [True, True], [False, False]]
    output = generate_or_truth_table(inputs)
    print(output)