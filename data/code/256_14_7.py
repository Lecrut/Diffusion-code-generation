from datetime import date

class DataRangeFinder:
    @staticmethod
    def find_range_integers(numbers):
        return max(numbers) - min(numbers)

    @staticmethod
    def find_range_floats(numbers):
        return max(numbers) - min(numbers)

    @staticmethod
    def find_range_dates(dates):
        return (max(dates) - min(dates)).days

if __name__ == '__main__':
    int_numbers = [10, 20, 30, 40, 50]
    float_numbers = [1.1, 2.2, 3.3, 4.4, 5.5]
    date_objects = [date(2020, 1, 1), date(2021, 1, 1), date(2022, 1, 1)]

    print("Range of integers:", DataRangeFinder.find_range_integers(int_numbers))
    print("Range of floats:", DataRangeFinder.find_range_floats(float_numbers))
    print("Range of dates (in days):", DataRangeFinder.find_range_dates(date_objects))