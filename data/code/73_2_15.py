from datetime import datetime

class TimeCalculator:
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24

    def calculate_difference(self, time1: datetime, time2: datetime) -> str:
        delta = abs(time2 - time1)
        days = delta.days
        seconds = delta.seconds
        hours = seconds // (self.SECONDS_PER_MINUTE * self.MINUTES_PER_HOUR)
        minutes = (seconds % (self.SECONDS_PER_MINUTE * self.MINUTES_PER_HOUR)) // self.SECONDS_PER_MINUTE
        remaining_seconds = seconds % self.SECONDS_PER_MINUTE

        return f"{days} days, {hours} hours, {minutes} minutes, {remaining_seconds} seconds"

if __name__ == '__main__':
    calculator = TimeCalculator()
    date1 = datetime(2023, 1, 1, 10, 0, 0)
    date2 = datetime(2023, 1, 5, 14, 30, 0)
    difference = calculator.calculate_difference(date1, date2)
    print(f"Time 1: {date1}")
    print(f"Time 2: {date2}")
    print(f"Difference: {difference}")