import datetime
import calendar

class MonthWeekdayCounter:
    WEEKEND_DAYS = {5, 6}
    WEEKDAY_THRESHOLD = 5

    @staticmethod
    def get_days_in_month(year: int, month: int) -> int:
        return calendar.monthrange(year, month)[1]

    @staticmethod
    def is_weekday(date_obj: datetime.date) -> bool:
        return date_obj.weekday() < MonthWeekdayCounter.WEEKDAY_THRESHOLD

    def count_weekdays_left(self, reference_date: datetime.date) -> int:
        year = reference_date.year
        month = reference_date.month
        day = reference_date.day
        days_in_month = self.get_days_in_month(year, month)
        
        if day > days_in_month:
            return 0
            
        end_date = datetime.date(year, month, days_in_month)
        count = 0
        current = reference_date
        
        while current <= end_date:
            if self.is_weekday(current):
                count += 1
            current += datetime.timedelta(days=1)
            
        return count

if __name__ == '__main__':
    ref_date = datetime.date(2023, 10, 15)
    counter = MonthWeekdayCounter()
    result = counter.count_weekdays_left(ref_date)
    print(result)