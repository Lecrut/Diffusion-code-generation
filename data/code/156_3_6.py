class MeanCalculator:
    @staticmethod
    def validate_input(values):
        if not isinstance(values, list) or len(values) == 0:
            raise ValueError("Input must be a non-empty list of floats")
    
    @staticmethod
    def calculate_mean(numbers):
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5]
    MeanCalculator.validate_input(sample_values)
    result = MeanCalculator.calculate_mean(sample_values)
    print(result)