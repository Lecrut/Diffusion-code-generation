def validate_exact_match(arg1, arg2):
    return arg1 == arg2

class MatchValidator:
    def __init__(self):
        self.match_cases = {
            'case1': (42, 42),
            'case2': ('hello', 'world'),
            'case3': ([1, 2, 3], [1, 2, 3]),
            'case4': ({'a': 1}, {'a': 1}),
        }

    def validate_all_cases(self):
        results = {key: validate_exact_match(*value) for key, value in self.match_cases.items()}
        return results

if __name__ == '__main__':
    validator = MatchValidator()
    results = validator.validate_all_cases()
    for case, result in results.items():
        print(f"Result for {case}: {result}")