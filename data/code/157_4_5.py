class NumericUtils:
    @staticmethod
    def validate_input(numbers):
        if not all(isinstance(n, (int, float)) for n in numbers):
            raise ValueError("All elements in the list must be numeric")

    @classmethod
    def find_smallest_value(cls, numbers):
        cls.validate_input(numbers)
        return min(numbers)

if __name__ == '__main__':
    sample_values = [-5, 3, -1, 2, -4]
    print(NumericUtils.find_smallest_value(sample_values))