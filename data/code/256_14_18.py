from datetime import date

class DataRangeFinder:
    @staticmethod
    def find_range_integers(int_list):
        return min(int_list), max(int_list)

    @staticmethod
    def find_range_floats(float_list):
        return min(float_list), max(float_list)

    @staticmethod
    def find_range_dates(date_list):
        return min(date_list), max(date_list)

if __name__ == '__main__':
    int_data = [10, 20, 30, 40, 50]
    float_data = [1.1, 2.2, 3.3, 4.4, 5.5]
    date_data = [date(2020, 1, 1), date(2021, 1, 1), date(2022, 1, 1)]

    print("Range of integers:", DataRangeFinder.find_range_integers(int_data))
    print("Range of floats:", DataRangeFinder.find_range_floats(float_data))
    print("Range of dates:", DataRangeFinder.find_range_dates(date_data))