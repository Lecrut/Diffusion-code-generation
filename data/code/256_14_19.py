from datetime import date

class DataRangeFinder:
    def find_int_range(self, data):
        return (min(data), max(data))

    def find_float_range(self, data):
        return (min(data), max(data))

    def find_date_range(self, data):
        return (min(data), max(data))

if __name__ == '__main__':
    finder = DataRangeFinder()
    
    int_data = [10, 20, 30, 40, 50]
    float_data = [1.1, 2.2, 3.3, 4.4, 5.5]
    date_data = [date(2020, 1, 1), date(2021, 1, 1), date(2022, 1, 1)]
    
    print(finder.find_int_range(int_data))
    print(finder.find_float_range(float_data))
    print(finder.find_date_range(date_data))