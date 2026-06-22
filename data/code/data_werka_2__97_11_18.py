def generate_or_truth_table(combinations):
    results = []
    for combo in combinations:
        if len(combo) != 2:
            raise ValueError("Each combination must have exactly two inputs")
        if not all(isinstance(x, bool) for x in combo):
            raise ValueError("Inputs must be boolean")
        results.append(combo[0] or combo[1])
    return results

if __name__ == '__main__':
    inputs = [[True, False], [False, True], [True, True], [False, False]]
    output = generate_or_truth_table(inputs)
    print(output)