class Validator:
    POSITIVE_THRESHOLD = 0
    EVEN_CHECK = 2
    MAX_VALUE = 100

    def __init__(self):
        self._history = []

    def _check_value(self, val):
        if val <= self.POSITIVE_THRESHOLD:
            return "not positive"
        if val % self.EVEN_CHECK != 0:
            return "odd"
        if val >= self.MAX_VALUE:
            return "too large"
        return "valid"

    def combine_and_report(self, a, b, c):
        checks = [self._check_value(x) for x in [a, b, c]]
        report = {
            "inputs": [a, b, c],
            "status": {
                "a": checks[0],
                "b": checks[1],
                "c": checks[2]
            },
            "all_valid": all(s == "valid" for s in checks)
        }
        self._history.append(report)
        return report

if __name__ == '__main__':
    validator = Validator()
    result1 = validator.combine_and_report(10, 20, 30)
    print(result1)
    result2 = validator.combine_and_report(-5, 101, 7)
    print(result2)
    print(validator._history)