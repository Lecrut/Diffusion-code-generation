import calendar
import datetime

class TimeCalculator:
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    SECONDS_PER_MINUTE = 60

    @staticmethod
    def _get_days_in_month(year, month):
        return calendar.monthrange(year, month)[1]

    @staticmethod
    def _get_current_datetime():
        return datetime.datetime.now()

    def calculate_remaining_minutes(self):
        now = self._get_current_datetime()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        second = now.second

        days_in_month = self._get_days_in_month(year, month)
        days_remaining = days_in_month - day
        if days_remaining < 0:
            days_remaining = 0

        hours_remaining_in_day = self.HOURS_PER_DAY - hour - 1
        if hours_remaining_in_day < 0:
            hours_remaining_in_day = 0

        minutes_remaining_in_hour = self.MINUTES_PER_HOUR - minute - 1
        if minutes_remaining_in_hour < 0:
            minutes_remaining_in_hour = 0

        total_remaining_minutes = (days_remaining * self.HOURS_PER_DAY * self.MINUTES_PER_HOUR) + (hours_remaining_in_day * self.MINUTES_PER_HOUR) + minutes_remaining_in_hour

        if second > 0:
            total_remaining_minutes += 1

        return total_remaining_minutes

if __name__ == '__main__':
    calculator = TimeCalculator()
    result = calculator.calculate_remaining_minutes()
    print(result)