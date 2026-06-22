class DateProcessor:
    _LEAP_THRESHOLD_4 = 4
    _LEAP_THRESHOLD_100 = 100
    _LEAP_THRESHOLD_400 = 400
    _MONTHS_DAYS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    @staticmethod
    def _is_leap_year(year):
        return (year % DateProcessor._LEAP_THRESHOLD_4 == 0 and year % DateProcessor._LEAP_THRESHOLD_100 != 0) or (year % DateProcessor._LEAP_THRESHOLD_400 == 0)

    @classmethod
    def get_day_of_month(cls, date_obj):
        if not hasattr(date_obj, 'year') or not hasattr(date_obj, 'month') or not hasattr(date_obj, 'day'):
            raise ValueError("Object must have year, month, and day attributes")
        
        year = date_obj.year
        month = date_obj.month
        day = date_obj.day

        if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
            raise ValueError("Year, month, and day must be integers")
        
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12")
        
        if day < 1:
            raise ValueError("Day must be positive")

        max_day = cls._MONTHS_DAYS[month]
        
        if month == 2 and cls._is_leap_year(year):
            max_day += 1
            
        if day > max_day:
            raise ValueError("Day out of range for the given month and year")

        return day

if __name__ == '__main__':
    import datetime
    sample_date = datetime.date(2024, 2, 29)
    processor = DateProcessor()
    result = processor.get_day_of_month(sample_date)
    print(result)