class MonthTimeCalculator:
    SECONDS_PER_DAY = 86400
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    def __init__(self, start_date, end_date):
        if start_date > end_date:
            raise ValueError("Start date must be before or equal to end date")
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    def _parse_date(date_str):
        parts = date_str.split('-')
        return int(parts[0]), int(parts[1]), int(parts[2])

    def calculate_remaining_time(self):
        start_y, start_m, start_d = self._parse_date(self.start_date)
        end_y, end_m, end_d = self._parse_date(self.end_date)
        
        start_total_days = self._to_days(start_y, start_m, start_d)
        end_total_days = self._to_days(end_y, end_m, end_d)
        
        delta_days = end_total_days - start_total_days
        
        days = delta_days
        hours = 0
        minutes = 0
        seconds = 0
        
        if delta_days > 0:
            days = delta_days - 1
            hours = 23
            minutes = 59
            seconds = 59
        else:
            hours = 23
            minutes = 59
            seconds = 59
            
        total_seconds = (days * self.SECONDS_PER_DAY) + (hours * self.SECONDS_PER_HOUR) + (minutes * self.SECONDS_PER_MINUTE) + seconds
        
        return {
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds,
            "total_seconds": total_seconds
        }

    def _to_days(self, y, m, d):
        return y * 365 + y // 4 - y // 100 + y // 400 + self._month_days(m) + d

    def _month_days(self, m):
        days_in_months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        return days_in_months[m - 1]

if __name__ == '__main__':
    calc = MonthTimeCalculator("2023-10-01", "2023-10-31")
    print(calc.calculate_remaining_time())
    
    calc2 = MonthTimeCalculator("2023-10-01", "2023-10-01")
    print(calc2.calculate_remaining_time())