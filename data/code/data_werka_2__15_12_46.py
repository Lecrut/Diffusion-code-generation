def validate_exact_match(arg1, arg2):
    return arg1 == arg2

class ExactMatchChecker:

    def __init__(self):
        self.match_results = {}

    def add_and_check(self, arg1, arg2):
        result = validate_exact_match(arg1, arg2)
        self.match_results[arg1, arg2] = result
        return result
if __name__ == '__main__':
    checker = ExactMatchChecker()
    pair1_result = checker.add_and_check('hello', 'hello')
    pair2_result = checker.add_and_check(42, 43)
    pair3_result = checker.add_and_check([1, 2, 3], [1, 2, 3])
    print(f"Result for ('hello', 'hello'): {pair1_result}")
    print(f'Result for (42, 43): {pair2_result}')
    print(f'Result for ([1, 2, 3], [1, 2, 3]): {pair3_result}')