class Validator:
    _MIN_POSITIVE = 1
    _MAX_LIMIT = 100
    _EVEN_THRESHOLD = 0

    @staticmethod
    def _check_value(val):
        issues = []
        if val <= Validator._MIN_POSITIVE:
            issues.append('not positive')
        if val % 2 != Validator._EVEN_THRESHOLD:
            issues.append('not even')
        if val >= Validator._MAX_LIMIT:
            issues.append('too large')
        return issues

    def combine_and_report(self, x, y, z):
        inputs = {'x': x, 'y': y, 'z': z}
        status_map = {}
        combined_sum = 0
        
        for k, v in inputs.items():
            if not isinstance(v, int):
                raise ValueError(f"Input {k} must be an integer")
            combined_sum += v
            status_map[k] = self._check_value(v)
        
        total_issues_count = sum(len(issues) for issues in status_map.values())
        
        report = {
            'inputs': inputs,
            'sum': combined_sum,
            'details': status_map,
            'validity': 'clean' if total_issues_count == 0 else 'issues_found'
        }
        
        return report

if __name__ == '__main__':
    validator = Validator()
    result = validator.combine_and_report(10, 25, 105)
    print(result)