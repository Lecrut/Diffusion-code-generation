import statistics

class AverageCalculator:
    @staticmethod
    def calculate_average(numbers):
        if not numbers:
            return 0
        return statistics.mean(numbers)

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_values = {
        'list1': [1, 2, 3, 4, 5],
        'list2': [10.5, 20.5, 30.5],
        'empty_list': [],
        'list3': [-10, 20, 30]
    }
    for name, value in sample_values.items():
        print(f"Average of {name}: {calculator.calculate_average(value)}")