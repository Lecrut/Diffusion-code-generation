class Validator:
    _CHECKS = {
        "positive": lambda x: x > 0,
        "even": lambda x: x % 2 == 0,
        "magnitude": lambda x: x < 100,
    }
    _LABELS = {
        "positive": "not positive",
        "even": "not even",
        "magnitude": "too large",
    }

    def combine_and_report(self, a, b, c):
        inputs = {"a": a, "b": b, "c": c}
        reports = []
        for name, val in inputs.items():
            for check_key, is_valid in self._CHECKS.items():
                if not is_valid(val):
                    reports.append(f"{name} is {self._LABELS[check_key]}")
        return {"inputs": inputs, "reports": reports}

if __name__ == '__main__':
    validator = Validator()
    result = validator.combine_and_report(10, 25, -5)
    print(result)