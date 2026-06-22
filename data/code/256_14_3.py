from datetime import date

class DataRangeCalculator:
    def calculate_range_integers(self, integers):
        return max(integers) - min(integers)

    def calculate_range_floats(self, floats):
        return max(floats) - min(floats)

    def calculate_range_dates(self, dates):
        return (max(dates) - min(dates)).days

if __name__ == '__main__':
    calculator = DataRangeCalculator()
    integers = [10, 25, 45]
    floats = [1.1, 3.3, 5.5]
    dates = [date(2020, 1, 1), date(2020, 6, 1), date(2020, 12, 31)]
    print(calculator.calculate_range_integers(integers))
    print(calculator.calculate_range_floats(floats))
    print(calculator.calculate_range_dates(dates))