class OddnessValidator:
    def is_odd(self, value):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            return False
        if isinstance(value, int):
            return abs(value) % 2 != 0
        elif isinstance(value, float):
            return round(abs(value)) % 2 != 0
    def validate_list(self, numbers):
        results = []
        for num in numbers:
            try:
                if self.is_odd(num):
                    results.append(True)
                else:
                    results.append(False)
            except Exception:
                results.append(None)
        return results
if __name__ == '__main__':
    validator = OddnessValidator()
    test_data = [1, 2, None, True, False, -3.5, -4, "odd", []]
    output = validator.validate_list(test_data)
    print(output)