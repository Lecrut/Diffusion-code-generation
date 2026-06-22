class DateValidator:
    DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    WEEKDAY_MASK = 0b111110
    WEEKEND_MASK = 0b000001

    @staticmethod
    def is_leap_year(year: int) -> bool:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @classmethod
    def get_days_in_month(cls, year: int, month: int) -> int:
        if month == 2 and cls.is_leap_year(year):
            return 29
        return cls.DAYS_IN_MONTH[month]

    @classmethod
    def is_valid_date(cls, year: int, month: int, day: int) -> bool:
        if month < 1 or month > 12:
            return False
        max_days = cls.get_days_in_month(year, month)
        return 1 <= day <= max_days

    @classmethod
    def _calculate_weekday(cls, year: int, month: int, day: int) -> int:
        if month < 3:
            month += 12
            year -= 1
        k = year % 100
        j = year // 100
        h = (day + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 - 2 * j) % 7
        return (h + 5) % 7

    @classmethod
    def is_weekday(cls, date_string: str) -> bool:
        if not isinstance(date_string, str):
            raise TypeError('Input must be a string')
        parts = date_string.split('-')
        if len(parts) != 3:
            raise ValueError('Date string must be in YYYY-MM-DD format')
        try:
            year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        except ValueError:
            raise ValueError('Date components must be integers')
        if not cls.is_valid_date(year, month, day):
            raise ValueError('Invalid date values')
        weekday_index = cls._calculate_weekday(year, month, day)
        return (weekday_index & cls.WEEKDAY_MASK) != 0

if __name__ == '__main__':
    sample_date = '2023-10-07'
    result = DateValidator.is_weekday(sample_date)
    print(result)