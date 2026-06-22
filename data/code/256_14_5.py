from datetime import date

class DataRangeFinder:

    def find_range_integers(self, integers):
        return max(integers) - min(integers)

    def find_range_floats(self, floats):
        return max(floats) - min(floats)

    def find_range_dates(self, dates):
        return (max(dates) - min(dates)).days
if __name__ == '__main__':
    finder = DataRangeFinder()
    integers = [10, 20, 30, 40, 50]
    floats = [1.5, 2.5, 3.5, 4.5, 5.5]
    dates = [date(2020, 1, 1), date(2020, 1, 15), date(2020, 2, 1)]
    print(finder.find_range_integers(integers))
    print(finder.find_range_floats(floats))
    print(finder.find_range_dates(dates))