class YearDurationCalculator:
    def __init__(self, days: int, hours_per_day: int, minutes_per_hour: int, seconds_per_minute: int):
        self.days = days
        self.hours_per_day = hours_per_day
        self.minutes_per_hour = minutes_per_hour
        self.seconds_per_minute = seconds_per_minute

    def calculate_seconds(self) -> int:
        return self.days * self.hours_per_day * self.minutes_per_hour * self.seconds_per_minute

    def get_breakdown(self) -> dict:
        return {
            'days': self.days,
            'hours': self.days * self.hours_per_day,
            'minutes': self.days * self.hours_per_day * self.minutes_per_hour,
            'seconds': self.calculate_seconds()
        }

if __name__ == '__main__':
    non_leap_year = YearDurationCalculator(365, 24, 60, 60)
    total_seconds = non_leap_year.calculate_seconds()
    print(total_seconds)
    breakdown = non_leap_year.get_breakdown()
    print(breakdown['minutes'])
    print(breakdown['hours'])