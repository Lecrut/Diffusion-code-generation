class DataRangeCalculator:
    @staticmethod
    def calculate_data_range(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        return max(data) - min(data)

if __name__ == '__main__':
    calculator = DataRangeCalculator()
    sample1 = [1, 5, 2, 8, 3]
    sample2 = [-10, 0, 5, -5]
    try:
        range1 = calculator.calculate_data_range(sample1)
        print(f"Data: {sample1}, Range: {range1}")
        range2 = calculator.calculate_data_range(sample2)
        print(f"Data: {sample2}, Range: {range2}")
    except ValueError as e:
        print(f"Error caught: {e}")