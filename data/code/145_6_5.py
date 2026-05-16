def generate_and_test_booleans(variables):
    n = len(variables)
    num_outcomes = 2 ** n
    results = []
    for i in range(num_outcomes):
        current_outcome = []
        temp_i = i
        for j in range(n):
            current_outcome.append(bool(temp_i % 2))
            temp_i //= 2
        results.append(tuple(current_outcome))
    return results
if __name__ == '__main__':
    sample_variables = [True, False, True]
    all_outcomes = generate_and_test_booleans(sample_variables)
    print("Input Variables:", sample_variables)
    print("Total Outcomes:", len(all_outcomes))
    print("All Outcomes:")
    for outcome in all_outcomes:
        print(outcome)