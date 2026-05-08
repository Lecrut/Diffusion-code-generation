def generate_and_test_boolean_outcomes(variables):
    n = len(variables)
    num_outcomes = 2 ** n
    results = []
    for i in range(num_outcomes):
        outcome = []
        temp = i
        for j in range(n):
            outcome.append(bool(temp % 2))
            temp //= 2
        results.append(tuple(outcome))
    return results
if __name__ == '__main__':
    sample_variables = [True, False, True]
    all_outcomes = generate_and_test_boolean_outcomes(sample_variables)
    print(f"Input variables: {sample_variables}")
    print(f"Total number of outcomes: {len(all_outcomes)}")
    print("All possible outcomes:")
    for outcome in all_outcomes:
        print(outcome)