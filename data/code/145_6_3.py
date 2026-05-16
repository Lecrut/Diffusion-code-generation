def generate_and_test_booleans(variables):
    n = len(variables)
    num_outcomes = 2 ** n
    results = []
    for i in range(num_outcomes):
        current_outcome = []
        temp = i
        for j in range(n):
            current_outcome.append(bool(temp % 2))
            temp //= 2
        results.append(current_outcome)
    return results
if __name__ == '__main__':
    input_vars = [True, False, True]
    all_outcomes = generate_and_test_booleans(input_vars)
    print("Input Variables:", input_vars)
    print("Total Outcomes:", len(all_outcomes))
    print("All Outcomes:")
    for outcome in all_outcomes:
        print(outcome)