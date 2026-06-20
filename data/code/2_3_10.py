class PalindromeChecker:
    def __init__(self, test_cases):
        self.test_cases = test_cases

    def check(self):
        results = {}
        for name, value in self.test_cases.items():
            results[name] = value == value[::-1]
        return results

if __name__ == '__main__':
    samples = {
        "level": "level",
        "world": "world",
        "deified": "deified",
        "test": "test"
    }
    checker = PalindromeChecker(samples)
    output = checker.check()
    for name, result in output.items():
        print(f"{name}: {result}")