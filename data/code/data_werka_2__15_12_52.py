def validate_exact_match(arg1, arg2):
    return arg1 == arg2

class MatchChecker:
    def __init__(self):
        self.match_cases = {
            'case1': ('hello', 'hello'),
            'case2': (42, 42),
            'case3': ([1, 2, 3], [1, 2, 3]),
            'case4': ("world", "hello")
        }
    
    def check_all_cases(self):
        results = {key: validate_exact_match(*value) for key, value in self.match_cases.items()}
        return results

if __name__ == '__main__':
    checker = MatchChecker()
    results = checker.check_all_cases()
    for case, result in results.items():
        print(f"Result for {case}: {result}")