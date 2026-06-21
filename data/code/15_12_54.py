def validate_exact_match(arg1, arg2):
    return arg1 == arg2

class MatchVerifier:

    def __init__(self):
        self.results = []

    def verify(self, arg1, arg2):
        result = validate_exact_match(arg1, arg2)
        self.results.append((arg1, arg2, result))
        return result

    def get_results_summary(self):
        summary = {pair: result for pair, _, result in self.results}
        return summary
if __name__ == '__main__':
    verifier = MatchVerifier()
    result1 = verifier.verify('hello', 'hello')
    result2 = verifier.verify(42, 43)
    result3 = verifier.verify([1, 2, 3], [1, 2, 3])
    print(f"Result for ('hello', 'hello'): {result1}")
    print(f'Result for (42, 43): {result2}')
    print(f'Result for ([1, 2, 3], [1, 2, 3]): {result3}')
    summary = verifier.get_results_summary()
    for pair, result in summary.items():
        print(f'Summary for {pair}: {result}')