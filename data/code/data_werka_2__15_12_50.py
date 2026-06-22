def validate_exact_match(arg1, arg2):
    return arg1 == arg2

class MatchChecker:
    def __init__(self):
        self.results = []

    def check(self, arg1, arg2):
        result = validate_exact_match(arg1, arg2)
        self.results.append((arg1, arg2, result))
        return result

    def print_results(self):
        for arg1, arg2, result in self.results:
            print(f"Result for {arg1} and {arg2}: {result}")

if __name__ == '__main__':
    checker = MatchChecker()
    
    sample_value1 = "hello"
    sample_value2 = "hello"
    checker.check(sample_value1, sample_value2)
    
    sample_value3 = 42
    sample_value4 = 42.0
    checker.check(sample_value3, sample_value4)
    
    sample_value5 = [1, 2, 3]
    sample_value6 = [1, 2, 3]
    checker.check(sample_value5, sample_value6)
    
    checker.print_results()