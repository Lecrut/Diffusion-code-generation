class Utility:
    @staticmethod
    def validate_number(value):
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be an integer or float")

    @staticmethod
    def is_negative(number):
        Utility.validate_number(number)
        return number < 0

if __name__ == '__main__':
    sample_values = [15, -8, 0, -2.7, 3]
    results = {value: Utility.is_negative(value) for value in sample_values}
    print(results)