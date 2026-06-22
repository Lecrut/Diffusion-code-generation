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
    print(finder.find_range_integers([1, 2, 3, 4, 5]))
    print(finder.find_range_floats([1.1, 2.2, 3.3, 4.4, 5.5]))
    print(finder.find_range_dates([date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)]))