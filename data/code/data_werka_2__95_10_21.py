class Validator:
    _MIN_POSITIVE = 1
    _MAX_LIMIT = 100

    @staticmethod
    def _validate_number(value):
        if not isinstance(value, int):
            raise TypeError("Input must be an integer")
        if value <= 0:
            raise ValueError("Input must be positive")
        if value >= Validator._MAX_LIMIT:
            raise ValueError("Input must be less than 100")
        if value % 2 != 0:
            raise ValueError("Input must be even")
        return True

    def combine_and_report(self, a, b, c):
        inputs = {'a': a, 'b': b, 'c': c}
        statuses = {}
        try:
            for key, val in inputs.items():
                self._validate_number(val)
                statuses[key] = "valid"
        except (ValueError, TypeError) as e:
            key = list(inputs.keys())[list(inputs.values()).index(val)] if val in inputs.values() else 'unknown'
            for k, v in inputs.items():
                if v == val:
                    key = k
                    break
            statuses[key] = str(e)
            for k, v in inputs.items():
                if k != key:
                    statuses[k] = "skipped"
            return {
                'inputs': inputs,
                'status': statuses,
                'valid_inputs': [k for k, v in statuses.items() if v == 'valid']
            }
        return {
            'inputs': inputs,
            'status': statuses,
            'valid_inputs': list(inputs.keys())
        }

if __name__ == '__main__':
    validator = Validator()
    result = validator.combine_and_report(20, 40, 60)
    print(result)
    
    try:
        result2 = validator.combine_and_report(15, 20, 40)
        print(result2)
    except ValueError as e:
        print(f"Caught error: {e}")
        result2 = validator.combine_and_report(15, 20, 40)
        print(result2)