class NumberUtility:
    @staticmethod
    def check_negativity(value):
        """Returns True if value is strictly negative, False otherwise."""
        return isinstance(value, (int, float)) and value < 0

if __name__ == '__main__':
    test_values = [5, -3.5, 0, -10]

    for val in test_values:
        result = NumberUtility.check_negativity(val)
        print(f"{val} is negative: {result}")