class AverageCalculator:
    def calculate_average(self, data: list[float]) -> float:
        if not data:
            raise ValueError("Input list cannot be empty.")
        return sum(data) / len(data)

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_data = [10.5, 20.0, 35.5, 40.0, 5.5]
    average = calculator.calculate_average(sample_data)
    print(f"The average of the sample data is: {average}")