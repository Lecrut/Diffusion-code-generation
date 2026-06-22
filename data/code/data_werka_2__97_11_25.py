def evaluate_or_combinations(combinations):
    if not combinations:
        return []
    table = []
    for combo in combinations:
        if not isinstance(combo, (list, tuple)) or len(combo) != 2:
            raise ValueError("Each combination must be a pair of booleans")
        first, second = combo
        table.append((first, second, first or second))
    return table

if __name__ == '__main__':
    test_cases = [[True, False], [False, True], [True, True], [False, False]]
    results = evaluate_or_combinations(test_cases)
    print(results)