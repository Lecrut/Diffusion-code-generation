class ValidationUtils:
    @staticmethod
    def is_negative(number):
        if not isinstance(number, (int, float)):
            raise ValueError("Input must be an integer or float.")
        return number < 0

if __name__ == '__main__':
    sample_values = [10, -5, 0, -3.5, 'a', None]
    results = {}
    for value in sample_values:
        try:
            results[value] = ValidationUtils.is_negative(value)
        except ValueError as e:
            results[value] = str(e)
    print(results)