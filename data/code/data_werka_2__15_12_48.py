def validate_exact_match(arg1, arg2):
    return arg1 == arg2

class MatchVerifier:
    def __init__(self):
        self.match_cases = {
            'case1': (42, 42),
            'case2': (3.14, 3.14),
            'case3': ("hello", "world"),
            'case4': ([1, 2, 3], [1, 2, 3])
        }
    
    def verify_all_cases(self):
        results = {key: validate_exact_match(*value) for key, value in self.match_cases.items()}
        return results

if __name__ == '__main__':
    verifier = MatchVerifier()
    results = verifier.verify_all_cases()
    for case, result in results.items():
        print(f"Result for {case}: {result}")