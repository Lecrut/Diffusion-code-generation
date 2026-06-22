class TimestampCalculator:
    def __init__(self, timestamp):
        if not isinstance(timestamp, (int, float)):
            raise ValueError("Timestamp must be numeric")
        if timestamp < 0:
            raise ValueError("Timestamp must be non-negative")
        self.timestamp = timestamp

    def get_day_of_month(self):
        total_seconds = int(self.timestamp)
        total_days = total_seconds // 86400
        year = 1970
        days_in_current_year = 365
        while True:
            is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            days_in_current_year = 366 if is_leap else 365
            if total_days < days_in_current_year:
                break
            total_days -= days_in_current_year
            year += 1
        
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if is_leap:
            month_days[1] = 29
        
        month = 0
        while month < 12:
            if total_days < month_days[month]:
                break
            total_days -= month_days[month]
            month += 1
        
        day = total_days + 1
        return day

if __name__ == '__main__':
    calc1 = TimestampCalculator(1672531200)
    print(calc1.get_day_of_month())
    
    calc2 = TimestampCalculator(0)
    print(calc2.get_day_of_month())
    
    calc3 = TimestampCalculator(1609459200)
    print(calc3.get_day_of_month())