class Validator:
    def __init__(self):
        self.threshold = 100
        self.min_positive = 1

    def _validate_single(self, value):
        status = "valid"
        reasons = []
        if value <= self.min_positive:
            status = "invalid"
            reasons.append("not positive")
        elif value % 2 != 0:
            status = "invalid"
            reasons.append("odd")
        elif value >= self.threshold:
            status = "invalid"
            reasons.append("too large")
        return status, reasons

    def combine_and_report(self, a, b, c):
        inputs = [a, b, c]
        reports = []
        for val in inputs:
            status, reasons = self._validate_single(val)
            reports.append({"value": val, "status": status, "reasons": reasons})
        
        combined_sum = sum(inputs)
        return {
            "inputs": inputs,
            "sum": combined_sum,
            "details": reports
        }

if __name__ == '__main__':
    validator = Validator()
    result = validator.combine_and_report(10, 25, 105)
    print(result)