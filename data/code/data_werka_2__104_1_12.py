class DateComparator:
    _MONTH_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    _SEPARATOR = '-'

    @staticmethod
    def _is_leap_year(year: int) -> bool:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def _parse_iso_date(date_str: str) -> tuple:
        parts = date_str.split(DateComparator._SEPARATOR)
        if len(parts) != 3:
            raise ValueError("Invalid ISO date format")
        try:
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
        except ValueError:
            raise ValueError("Invalid date components")
        
        if month < 1 or month > 12:
            raise ValueError("Invalid month")
        
        max_days = DateComparator._MONTH_DAYS[month]
        if month == 2 and DateComparator._is_leap_year(year):
            max_days = 29
        
        if day < 1 or day > max_days:
            raise ValueError("Invalid day")
        
        if year < 1:
            raise ValueError("Invalid year")
            
        return (year, month, day)

    @staticmethod
    def get_later_date(date1: str, date2: str) -> str:
        d1 = DateComparator._parse_iso_date(date1)
        d2 = DateComparator._parse_iso_date(date2)
        
        if d1 > d2:
            return date1
        elif d2 > d1:
            return date2
        else:
            return date1

if __name__ == '__main__':
    result = DateComparator.get_later_date("2023-02-28", "2024-02-29")
    print(result)