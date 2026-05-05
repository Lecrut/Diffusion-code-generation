from datetime import datetime
class TimeCalculator:
    def calculate_difference(self, time1: datetime, time2: datetime) -> datetime:
        return time2 - time1
if __name__ == '__main__':
    calculator = TimeCalculator()
    date1 = datetime(2023, 1, 1, 10, 0, 0)
    date2 = datetime(2023, 1, 5, 14, 30, 0)
    difference = calculator.calculate_difference(date1, date2)
    print(f"Time 1: {date1}")
    print(f"Time 2: {date2}")
    print(f"Difference: {difference}")