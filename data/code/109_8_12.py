class MonthWeekdayCounter:
    MONDAY = 0
    SUNDAY = 6
    WEEKEND_DAYS = {5, 6}

    @staticmethod
    def get_last_day_of_month(year, month):
        if month == 12:
            next_month = 1
            next_year = year + 1
        else:
            next_month = month + 1
            next_year = year
        first_day_next = __import__('datetime').date(next_year, next_month, 1)
        last_day_current = first_day_next - __import__('datetime').timedelta(days=1)
        return last_day_current.day

    def count_weekdays_left(self, ref_year, ref_month, ref_day):
        import datetime
        start_date = datetime.date(ref_year, ref_month, ref_day)
        last_day = self.get_last_day_of_month(ref_year, ref_month)
        end_date = datetime.date(ref_year, ref_month, last_day)
        
        if start_date > end_date:
            return 0
            
        count = 0
        current = start_date
        while current <= end_date:
            if current.weekday() not in self.WEEKEND_DAYS:
                count += 1
            current += datetime.timedelta(days=1)
        return count

if __name__ == '__main__':
    counter = MonthWeekdayCounter()
    ref_y = 2023
    ref_m = 10
    ref_d = 15
    result = counter.count_weekdays_left(ref_y, ref_m, ref_d)
    print(result)