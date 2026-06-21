def validate_exact_match(arg1, arg2):
    if not isinstance(arg1, type(arg2)):
        raise ValueError("Arguments must be of the same type")
    return arg1 == arg2

class MatchValidator:
    def __init__(self):
        self.matches = []

    def add_pair(self, arg1, arg2):
        try:
            is_match = validate_exact_match(arg1, arg2)
            self.matches.append((arg1, arg2, is_match))
        except ValueError as e:
            print(f"Error adding pair ({arg1}, {arg2}): {e}")

    def check_all_matches(self):
        return {pair[:2]: pair[2] for pair in self.matches}

if __name__ == '__main__':
    validator = MatchValidator()
    validator.add_pair("hello", "hello")
    validator.add_pair(42, 43)
    validator.add_pair([1, 2, 3], [1, 2, 3])
    results = validator.check_all_matches()
    for pair, result in results.items():
        print(f"Result for {pair}: {result}")