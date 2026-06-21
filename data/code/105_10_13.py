from datetime import datetime

class DateCalculator:
    DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    @staticmethod
    def _is_leap_year(year: int) -> bool:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def get_days_in_month(year: int, month: int) -> int:
        if month == 2:
            return 29 if DateCalculator._is_leap_year(year) else 28
        return DateCalculator.DAYS_IN_MONTH[month]

    def get_next_day(self, date_str: str) -> datetime:
        parts = date_str.split('-')
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        
        max_day = self.get_days_in_month(year, month)
        
        next_day = day + 1
        next_month = month
        next_year = year
        
        if next_day > max_day:
            next_day = 1
            next_month += 1
            if next_month > 12:
                next_month = 1
                next_year += 1
        
        return datetime(next_year, next_month, next_day)

if __name__ == '__main__':
    calculator = DateCalculator()
    sample_date = '2024-02-28'
    result = calculator.get_next_day(sample_date)
    print(result)