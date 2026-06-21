def validate_exact_match(arg1, arg2):
    if not isinstance(arg1, type(arg2)):
        raise ValueError("Arguments must be of the same type")
    return arg1 == arg2

class MatchValidator:
    def __init__(self):
        self.match_results = {}

    def add_pair(self, arg1, arg2):
        try:
            result = validate_exact_match(arg1, arg2)
            self.match_results[(arg1, arg2)] = result
        except ValueError as e:
            self.match_results[(arg1, arg2)] = str(e)

    def get_all_results(self):
        return self.match_results

if __name__ == '__main__':
    validator = MatchValidator()
    validator.add_pair("hello", "hello")
    validator.add_pair(42, 43)
    validator.add_pair([1, 2, 3], [1, 2, 3])
    validator.add_pair("test", 123)
    
    results = validator.get_all_results()
    for pair, result in results.items():
        print(f"Result for {pair}: {result}")