is_neg_lambda = lambda n: n < 0

if __name__ == "__main__":
    test_cases = [-1, -5, -234, 0, 1, 10]
    results = [test_case for test_case in test_cases if is_neg_lambda(test_case)] # This filters to only negatives.
    # Let's print the boolean result instead just to be clear on "returns a boolean value indicating".
    outputs = [(x, is_neg_lambda(x)) for x in test_cases]
    for val, res in outputs:
        print(f"Input: {val}, Is Negative: {res}")