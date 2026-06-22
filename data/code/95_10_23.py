class Validator:
    POSITIVE_THRESHOLD = 0
    MAX_MAGNITUDE = 100
    EVEN_MODULUS = 2

    def _validate_single(self, value):
        status = "valid"
        if value <= self.POSITIVE_THRESHOLD:
            status = "not positive"
        elif value % self.EVEN_MODULUS != 0:
            status = "odd"
        elif value >= self.MAX_MAGNITUDE:
            status = "too large"
        return status

    def combine_and_report(self, a, b, c):
        status_a = self._validate_single(a)
        status_b = self._validate_single(b)
        status_c = self._validate_single(c)

        combined_sum = a + b + c

        report = {
            "inputs": {
                "a": a,
                "b": b,
                "c": c
            },
            "statuses": {
                "a": status_a,
                "b": status_b,
                "c": status_c
            },
            "combined_sum": combined_sum
        }
        return report

if __name__ == '__main__':
    validator_instance = Validator()
    result = validator_instance.combine_and_report(10, 25, 105)
    print(result)