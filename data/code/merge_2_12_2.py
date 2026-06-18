class OddnessValidator:
    def is_odd(self, value):
        if not isinstance(value, (int, float)):
            return False
        if isinstance(value, bool):
            return False
        if value % 2 != 0:
            return True
        return False
    def validate_list(self, numbers):
        results = []
        for num in numbers:
            try:
                is_odd_result = self.is_odd(num)
                results.append(is_odd_result)
            except Exception:
                results.append(None)
        return results
if __name__ == '__main__':
    validator = OddnessValidator()
    test_data = [1, 2.5, -3, None, True, False, "a", 0]
    output = validator.validate_list(test_data)
    print(output)