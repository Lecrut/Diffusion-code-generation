class SequenceCalculator:
    ERROR_MESSAGE = "Invalid input: Expected a sequence of integers"

    @staticmethod
    def is_valid_sequence(data):
        return isinstance(data, list) and all(isinstance(item, int) for item in data)

    @classmethod
    def calculate_sum(cls, data):
        if cls.is_valid_sequence(data):
            return sum(data)
        else:
            print(cls.ERROR_MESSAGE)
            return None

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    calculator = SequenceCalculator()
    result = calculator.calculate_sum(sample_data)
    if result is not None:
        print(result)