import statistics

class AverageCalculator:
    @staticmethod
    def calculate_average(numbers):
        if not numbers:
            raise ValueError("Input list is empty")
        return statistics.mean(numbers)

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_data = [
        [1.0, 2.0, 3.0],
        [10.5, 20.5, 30.5, 40.5],
        [5.5],
        [],
        [1.0, 1.0, 1.0, 1.0]
    ]
    try:
        for data_set in sample_data:
            avg = calculator.calculate_average(data_set)
            print(avg)
    except ValueError as e:
        print(e)