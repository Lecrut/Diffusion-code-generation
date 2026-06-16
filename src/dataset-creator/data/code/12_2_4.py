class OddnessValidator:
    def validate(self, numbers):
        result = []
        for num in numbers:
            if isinstance(num, bool) or not isinstance(num, (int, float)):
                continue
            try:
                is_odd = abs(int(num)) % 2 != 0
                result.append((num, is_odd))
            except ValueError:
                pass
        return result
if __name__ == '__main__':
    test_data = [1, -3, None, True, False, "5", 4.7, 6]
    validator = OddnessValidator()
    output = validator.validate(test_data)
    print(output)