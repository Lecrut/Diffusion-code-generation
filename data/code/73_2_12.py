from datetime import datetime

class TimeCalculator:
    def calculate_difference(self, time1: datetime, time2: datetime) -> timedelta:
        return abs(time2 - time1)

if __name__ == '__main__':
    calculator = TimeCalculator()
    start_time = datetime(2023, 1, 1, 8, 0, 0)
    end_time = datetime(2023, 1, 1, 17, 45, 0)
    difference = calculator.calculate_difference(start_time, end_time)
    print(f"Start Time: {start_time}")
    print(f"End Time: {end_time}")
    print(f"Difference in hours and minutes: {(difference.seconds // 3600)} hours and {(difference.seconds % 3600) // 60} minutes")