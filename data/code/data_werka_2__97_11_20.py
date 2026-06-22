def compute_or_results(pairs):
    if not pairs:
        return []
    for pair in pairs:
        if len(pair) != 2:
            raise ValueError("Each combination must have exactly two boolean inputs")
    return [[x, y, x | y] for x, y in pairs]

if __name__ == '__main__':
    test_cases = [[True, False], [False, True], [True, True], [False, False]]
    final_output = compute_or_results(test_cases)
    print(final_output)