class Validator:
    _CHECKS = {
        "positive": lambda x: x > 0,
        "even": lambda x: x % 2 == 0,
        "small": lambda x: x < 100,
    }

    def combine_and_report(self, a, b, c):
        inputs = {"a": a, "b": b, "c": c}
        status = {}
        for key, value in inputs.items():
            checks = []
            for check_name, check_fn in self._CHECKS.items():
                if check_fn(value):
                    checks.append(check_name)
            if not checks:
                checks.append("invalid")
            status[key] = checks
        return {"inputs": inputs, "status": status}

if __name__ == '__main__':
    validator = Validator()
    result = validator.combine_and_report(10, 5, 105)
    print(result)