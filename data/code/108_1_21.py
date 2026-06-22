class DayOfMonthCalculator:
    DAYS_IN_MONTHS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    @staticmethod
    def _is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def get_day_of_month(timestamp):
        if not isinstance(timestamp, (int, float)):
            raise ValueError("Timestamp must be a number")
        if timestamp < 0:
            raise ValueError("Timestamp must be non-negative")
        
        seconds_per_day = 86400
        total_days = int(timestamp // seconds_per_day)
        
        year = 1970
        remaining_days = total_days
        
        while True:
            days_in_year = 366 if DayOfMonthCalculator._is_leap_year(year) else 365
            if remaining_days < days_in_year:
                break
            remaining_days -= days_in_year
            year += 1
        
        month = 1
        while True:
            days_in_current_month = DayOfMonthCalculator.DAYS_IN_MONTHS[month]
            if month == 2 and DayOfMonthCalculator._is_leap_year(year):
                days_in_current_month += 1
            
            if remaining_days < days_in_current_month:
                break
            remaining_days -= days_in_current_month
            month += 1
        
        day = remaining_days + 1
        return day

if __name__ == '__main__':
    calculator = DayOfMonthCalculator()
    print(calculator.get_day_of_month(1672531200))
    print(calculator.get_day_of_month(0))
    print(calculator.get_day_of_month(1609459200))