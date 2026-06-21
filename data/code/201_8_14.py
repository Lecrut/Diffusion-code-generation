class AverageCalculator:
    @staticmethod
    def calculate_average(data):
        if not data:
            raise ValueError("Input data cannot be empty.")
        return sum(data) / len(data)

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_data = {
        'set1': [1, 2, 3, 4, 5],
        'set2': [10.5, 20.5, 30.5],
        'set3': [-1, 0, 1, 2, -2],
        'set4': [100, 200, 300]
    }
    for key, values in sample_data.items():
        print(f"Average of {key}: {calculator.calculate_average(values)}")