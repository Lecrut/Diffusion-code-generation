def validate_exact_match(arg1, arg2):
    return arg1 == arg2

class ExactMatchValidator:
    def __init__(self):
        self.matches = []

    def add_pair(self, arg1, arg2):
        self.matches.append((arg1, arg2))

    def check_all_matches(self):
        results = {pair: validate_exact_match(*pair) for pair in self.matches}
        return results

if __name__ == '__main__':
    validator = ExactMatchValidator()
    validator.add_pair("hello", "hello")
    validator.add_pair(42, 43)
    validator.add_pair([1, 2, 3], [1, 2, 3])
    results = validator.check_all_matches()
    for pair, result in results.items():
        print(f"Result for {pair}: {result}")