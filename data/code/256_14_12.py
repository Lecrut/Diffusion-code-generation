from datetime import date

class DataRangeFinder:
    def find_range_integers(self, numbers):
        if not all(isinstance(n, int) for n in numbers):
            raise ValueError("All elements must be integers")
        return max(numbers) - min(numbers)

    def find_range_floats(self, numbers):
        if not all(isinstance(n, float) for n in numbers):
            raise ValueError("All elements must be floats")
        return max(numbers) - min(numbers)

    def find_range_dates(self, dates):
        if not all(isinstance(d, date) for d in dates):
            raise ValueError("All elements must be dates")
        return (max(dates) - min(dates)).days

if __name__ == '__main__':
    finder = DataRangeFinder()
    integers = [10, 20, 30, 40]
    floats = [1.5, 2.5, 3.5, 4.5]
    dates = [date(2020, 1, 1), date(2020, 12, 31)]
    
    print(finder.find_range_integers(integers))
    print(finder.find_range_floats(floats))
    print(finder.find_range_dates(dates))