from datetime import date

class DataRangeFinder:
    def find_range_integers(self, numbers):
        return (min(numbers), max(numbers))

    def find_range_floats(self, numbers):
        return (min(numbers), max(numbers))

    def find_range_dates(self, dates):
        return (min(dates), max(dates))

if __name__ == '__main__':
    finder = DataRangeFinder()
    integers = [10, 20, 30, 40, 50]
    floats = [1.1, 2.2, 3.3, 4.4, 5.5]
    dates = [date(2020, 1, 1), date(2021, 1, 1), date(2022, 1, 1)]
    
    print(finder.find_range_integers(integers))
    print(finder.find_range_floats(floats))
    print(finder.find_range_dates(dates))