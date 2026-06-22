import datetime
import calendar

class MonthSecondsCalculator:
    SECONDS_IN_MINUTE = 60
    MINUTES_IN_HOUR = 60
    HOURS_IN_DAY = 24
    SECONDS_IN_DAY = HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE

    @staticmethod
    def get_days_in_month(year, month):
        return calendar.monthrange(year, month)[1]

    def compute_remaining_seconds(self, year, month, day, hour, minute, second):
        current_dt = datetime.datetime(year, month, day, hour, minute, second)
        days_in_current_month = self.get_days_in_month(year, month)
        remaining_days_in_current = days_in_current_month - day
        if remaining_days_in_current < 0:
            remaining_days_in_current = 0
        
        remaining_seconds_today = (self.HOURS_IN_DAY - hour) * self.SECONDS_IN_DAY
        remaining_seconds_today -= (minute * self.SECONDS_IN_MINUTE)
        remaining_seconds_today -= second
        
        if remaining_seconds_today < 0:
            remaining_seconds_today = 0
            
        seconds_from_full_days = remaining_days_in_current * self.SECONDS_IN_DAY
        
        total_seconds = seconds_from_full_days + remaining_seconds_today
        return total_seconds

if __name__ == '__main__':
    calculator = MonthSecondsCalculator()
    result = calculator.compute_remaining_seconds(2023, 10, 15, 12, 30, 45)
    print(result)