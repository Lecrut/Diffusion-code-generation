from datetime import date

class DataRangeHandler:
    def calculate_range_integers(self, numbers):
        return max(numbers) - min(numbers)
    
    def calculate_range_floats(self, numbers):
        return max(numbers) - min(numbers)
    
    def calculate_range_dates(self, dates):
        return (max(dates) - min(dates)).days

if __name__ == '__main__':
    handler = DataRangeHandler()
    sample_integers = [50, 30, 70, 10]
    sample_floats = [2.3, 4.6, 1.9, 3.2]
    sample_dates = [date(2021, 1, 1), date(2021, 5, 15), date(2021, 12, 31)]
    
    print("Range of integers:", handler.calculate_range_integers(sample_integers))
    print("Range of floats:", handler.calculate_range_floats(sample_floats))
    print("Range of dates:", handler.calculate_range_dates(sample_dates))