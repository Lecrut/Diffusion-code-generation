class DateFormatter:
    MONTH_MAP = {
        '01': 1, '02': 2, '03': 3, '04': 4,
        '05': 5, '06': 6, '07': 7, '08': 8,
        '09': 9, '10': 10, '11': 11, '12': 12
    }

    @staticmethod
    def _validate_month(month_str: str) -> int:
        if month_str not in DateFormatter.MONTH_MAP:
            raise ValueError(f"Invalid month: {month_str}")
        return DateFormatter.MONTH_MAP[month_str]

    @staticmethod
    def _validate_day(day_str: str, month: int, year: int) -> int:
        day = int(day_str)
        if day < 1:
            raise ValueError("Day must be positive")
        
        if month in (1, 3, 5, 7, 8, 10, 12):
            max_days = 31
        elif month in (4, 6, 9, 11):
            max_days = 30
        else:
            is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            max_days = 29 if is_leap else 28
        
        if day > max_days:
            raise ValueError(f"Day {day} out of range for month {month} in year {year}")
        return day

    @staticmethod
    def convert(date_str: str) -> str:
        parts = date_str.split('/')
        if len(parts) != 3:
            raise ValueError("Date string must be in MM/DD/YYYY format")
        
        month_str, day_str, year_str = parts
        
        if len(year_str) != 4:
            raise ValueError("Year must be 4 digits")
        if not (month_str.isdigit() and day_str.isdigit()):
            raise ValueError("Month and day must be numeric")
            
        year = int(year_str)
        month = DateFormatter._validate_month(month_str)
        day = DateFormatter._validate_day(day_str, month, year)
        
        return f"{year}-{month:02d}-{day:02d}"

if __name__ == '__main__':
    input_date = "02/29/2024"
    formatted = DateFormatter.convert(input_date)
    print(formatted)