from datetime import date

class DateCalculator:
    STANDARD_YEAR_DAYS = 365
    LEAP_YEAR_DAYS = 366

    @staticmethod
    def _parse_date(date_str: str) -> date:
        parts = date_str.split('-')
        y = int(parts[0])
        m = int(parts[1])
        d = int(parts[2])
        return date(y, m, d)

    @staticmethod
    def _is_leap_year(year: int) -> bool:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @classmethod
    def get_year_difference(cls, start_date_str: str, end_date_str: str) -> int:
        start_date = cls._parse_date(start_date_str)
        end_date = cls._parse_date(end_date_str)
        
        if start_date > end_date:
            start_date, end_date = end_date, start_date
            
        years = end_date.year - start_date.year
        
        start_month_day = (start_date.month, start_date.day)
        end_month_day = (end_date.month, end_date.day)
        
        if end_month_day < start_month_day:
            years -= 1
            
        return years

if __name__ == '__main__':
    calc = DateCalculator()
    result = calc.get_year_difference("2020-02-29", "2024-02-28")
    print(result)