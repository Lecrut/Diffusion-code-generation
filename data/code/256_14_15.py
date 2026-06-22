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
    
    int_numbers = [10, 20, 30, 40, 50]
    float_numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
    date_objects = [date(2022, 1, 1), date(2022, 1, 15), date(2022, 2, 1)]
    
    print(finder.find_range_integers(int_numbers))
    print(finder.find_range_floats(float_numbers))
    print(finder.find_range_dates(date_objects))