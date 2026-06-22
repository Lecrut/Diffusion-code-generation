from datetime import date

class DataRangeAnalyzer:
    def calculate_range_integers(self, numbers):
        return max(numbers) - min(numbers)
    
    def calculate_range_floats(self, numbers):
        return max(numbers) - min(numbers)
    
    def calculate_range_dates(self, dates):
        return (max(dates) - min(dates)).days

if __name__ == '__main__':
    analyzer = DataRangeAnalyzer()
    integers = [10, 20, 30, 40]
    floats = [1.5, 2.5, 3.5, 4.5]
    dates = [date(2020, 1, 1), date(2020, 12, 31)]
    print(analyzer.calculate_range_integers(integers))
    print(analyzer.calculate_range_floats(floats))
    print(analyzer.calculate_range_dates(dates))