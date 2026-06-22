class StringLengthCalculator:
    def __init__(self):
        self.test_cases = ["hello", "", "Python is awesome!", "\n\t "]

    @staticmethod
    def calculate_length(s: str) -> int:
        return len(s)

    def run_tests(self):
        results = [(s, self.calculate_length(s)) for s in self.test_cases]
        return results

if __name__ == '__main__':
    calculator = StringLengthCalculator()
    print(calculator.run_tests())