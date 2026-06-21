class BooleanValidator:
    @staticmethod
    def validate_outcome(outcome):
        return all([not (x and y) for x, y in zip(outcome[:-1], outcome[1:])])

    @staticmethod
    def generate_and_test_boolean_outcomes(variables):
        n = len(variables)
        num_outcomes = 2 ** n
        results = []
        for i in range(num_outcomes):
            outcome = [bool(i & (1 << j)) for j in range(n)]
            if BooleanValidator.validate_outcome(outcome):
                results.append(tuple(reversed(outcome)))
        return results

if __name__ == '__main__':
    sample_variables = [True, False, True]
    all_valid_outcomes = BooleanValidator.generate_and_test_boolean_outcomes(sample_variables)
    print(f"Input variables: {sample_variables}")
    print(f"Total number of valid outcomes: {len(all_valid_outcomes)}")
    for outcome in all_valid_outcomes:
        print(outcome)