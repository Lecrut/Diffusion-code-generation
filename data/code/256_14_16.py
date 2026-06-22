from datetime import date

class DataRangeFinder:
    def find_range_integers(self, numbers):
        return max(numbers) - min(numbers)
    
    def find_range_floats(self, numbers):
        return max(numbers) - min(numbers)
    
    def find_range_dates(self, dates):
        return (max(dates) - min(dates)).days

if __name__ == '__main__':
    finder = DataRangeFinder()
    integers = [10, 25, 45]
    floats = [1.1, 3.3, 5.5]
    dates = [date(2020, 1, 1), date(2020, 6, 1), date(2020, 12, 31)]
    print(finder.find_range_integers(integers))
    print(finder.find_range_floats(floats))
    print(finder.find_range_dates(dates))