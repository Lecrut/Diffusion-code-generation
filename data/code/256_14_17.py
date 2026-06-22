from datetime import date

class DataRangeFinder:
    def find_range_integers(self, integers):
        return min(integers), max(integers)

    def find_range_floats(self, floats):
        return min(floats), max(floats)

    def find_range_dates(self, dates):
        return min(dates), max(dates)

if __name__ == '__main__':
    finder = DataRangeFinder()
    
    integers = [3, 1, 4, 1, 5, 9]
    floats = [2.718, 3.141, 0.577, 1.618]
    dates = [date(2020, 1, 1), date(2021, 1, 1), date(2019, 1, 1)]
    
    print(finder.find_range_integers(integers))
    print(finder.find_range_floats(floats))
    print(finder.find_range_dates(dates))