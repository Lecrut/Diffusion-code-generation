from datetime import date

class DataRangeFinder:
    def find_range_integers(self, numbers):
        return min(numbers), max(numbers)

    def find_range_floats(self, numbers):
        return min(numbers), max(numbers)

    def find_range_dates(self, dates):
        return min(dates), max(dates)

if __name__ == '__main__':
    finder = DataRangeFinder()
    
    int_numbers = [10, 20, 30, 40, 50]
    float_numbers = [1.1, 2.2, 3.3, 4.4, 5.5]
    date_objects = [date(2020, 1, 1), date(2021, 1, 1), date(2022, 1, 1)]
    
    print(finder.find_range_integers(int_numbers))
    print(finder.find_range_floats(float_numbers))
    print(finder.find_range_dates(date_objects))