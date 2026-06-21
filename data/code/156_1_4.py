class AverageCalculator:

    @staticmethod
    def calculate_average(data):
        if not data:
            raise ValueError('Input list cannot be empty')
        total = 0
        count = len(data)
        for number in data:
            total += number
        return total / count
if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_values1 = [1.0, 2.0, 3.0, 4.0, 5.0]
    sample_values2 = [10.5, 20.5, 30.5]
    empty_list = []
    try:
        avg1 = calculator.calculate_average(sample_values1)
        print(f'Average of {sample_values1}: {avg1}')
        avg2 = calculator.calculate_average(sample_values2)
        print(f'Average of {sample_values2}: {avg2}')
        calculator.calculate_average(empty_list)
    except ValueError as e:
        print(f'Error: {e}')