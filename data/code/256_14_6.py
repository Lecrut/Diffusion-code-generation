from datetime import date

class DataRangeAnalyzer:
    def validate_integers(self, numbers):
        if not all(isinstance(num, int) for num in numbers):
            raise ValueError("All elements must be integers")
    
    def validate_floats(self, numbers):
        if not all(isinstance(num, float) for num in numbers):
            raise ValueError("All elements must be floats")
    
    def validate_dates(self, dates):
        if not all(isinstance(d, date) for d in dates):
            raise ValueError("All elements must be dates")
    
    def find_range_integers(self, numbers):
        self.validate_integers(numbers)
        return max(numbers) - min(numbers)
    
    def find_range_floats(self, numbers):
        self.validate_floats(numbers)
        return max(numbers) - min(numbers)
    
    def find_range_dates(self, dates):
        self.validate_dates(dates)
        return (max(dates) - min(dates)).days

if __name__ == '__main__':
    analyzer = DataRangeAnalyzer()
    print(analyzer.find_range_integers([10, 20, 30, 40]))
    print(analyzer.find_range_floats([1.5, 2.5, 3.5, 4.5]))
    print(analyzer.find_range_dates([date(2020, 1, 1), date(2020, 12, 31)]))