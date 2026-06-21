def compute_or_table(combinations):
    table = []
    for inputs in combinations:
        left = inputs[0]
        right = inputs[1]
        combined = left or right
        table.append([left, right, combined])
    return table

if __name__ == '__main__':
    test_cases = [[True, True], [False, False], [True, False], [False, True]]
    result = compute_or_table(test_cases)
    print(result)