class NumericMeanCalculator:
    @staticmethod
    def calculate_mean(data):
        numeric_values = [item for item in data if isinstance(item, (int, float))]
        if not numeric_values:
            return None
        return sum(numeric_values) / len(numeric_values)

if __name__ == '__main__':
    sample_data = [10, "a", 25.5, None, 30, "hello", 4.5]
    calculator = NumericMeanCalculator()
    mean_value = calculator.calculate_mean(sample_data)
    print(mean_value)