from datetime import datetime

class TimeCalculator:
    def calculate_difference(self, time1: datetime, time2: datetime) -> str:
        difference = abs(time2 - time1)
        days = difference.days
        hours, remainder = divmod(difference.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{days}d {hours}h {minutes}m {seconds}s"

if __name__ == '__main__':
    calculator = TimeCalculator()
    start_time = datetime(2023, 1, 1, 9, 0, 0)
    end_time = datetime(2023, 1, 5, 18, 45, 0)
    result = calculator.calculate_difference(start_time, end_time)
    print(f"Start Time: {start_time}")
    print(f"End Time: {end_time}")
    print(f"Difference: {result}")