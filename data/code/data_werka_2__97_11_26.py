def generate_or_truth_table(combinations):
    results = []
    for combo in combinations:
        if len(combo) != 2:
            raise ValueError("Each combination must have exactly two boolean inputs")
        a, b = combo
        if not (isinstance(a, bool) and isinstance(b, bool)):
            raise ValueError("Inputs must be boolean values")
        results.append([a, b, a or b])
    return results

if __name__ == '__main__':
    inputs = [[True, True], [True, False], [False, True], [False, False]]
    output = generate_or_truth_table(inputs)
    print(output)