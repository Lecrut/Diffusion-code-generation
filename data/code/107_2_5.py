class TimestampParser:
    _SECONDS_PER_DAY = 86400
    _EPOCH_YEAR = 1970
    _MONTH_DAYS_COMMON = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    _MONTH_DAYS_LEAP = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    @staticmethod
    def _is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @classmethod
    def get_days_in_year(cls, year):
        if cls._is_leap_year(year):
            return 366
        return 365

    @classmethod
    def parse(cls, timestamp):
        if not isinstance(timestamp, int):
            raise ValueError("Timestamp must be an integer")
        if timestamp < 0:
            raise ValueError("Timestamp must be non-negative")
        
        total_days = timestamp // cls._SECONDS_PER_DAY
        year = cls._EPOCH_YEAR
        
        while True:
            days_in_year = cls.get_days_in_year(year)
            if total_days < days_in_year:
                break
            total_days -= days_in_year
            year += 1
        
        month_days = cls._MONTH_DAYS_LEAP if cls._is_leap_year(year) else cls._MONTH_DAYS_COMMON
        month = 1
        while month <= 12:
            if total_days < month_days[month]:
                break
            total_days -= month_days[month]
            month += 1
        
        day = total_days + 1
        return f"{year:04d}/{month:02d}/{day:02d}"

if __name__ == '__main__':
    print(TimestampParser.parse(0))
    print(TimestampParser.parse(86400))
    print(TimestampParser.parse(1356998400))
    print(TimestampParser.parse(1609459200))
    print(TimestampParser.parse(1640995200))
    print(TimestampParser.parse(1704067200))
    print(TimestampParser.parse(1735689600))
    print(TimestampParser.parse(1767225600))
    print(TimestampParser.parse(1798761600))
    print(TimestampParser.parse(1830384000))
    print(TimestampParser.parse(1861920000))
    print(TimestampParser.parse(1893456000))
    print(TimestampParser.parse(1924992000))
    print(TimestampParser.parse(1956614400))
    print(TimestampParser.parse(1988150400))
    print(TimestampParser.parse(2019686400))
    print(TimestampParser.parse(2051308800))
    print(TimestampParser.parse(2082844800))
    print(TimestampParser.parse(2114380800))
    print(TimestampParser.parse(2145916800))
    print(TimestampParser.parse(2177539200))
    print(TimestampParser.parse(2209075200))
    print(TimestampParser.parse(2240611200))
    print(TimestampParser.parse(2272233600))
    print(TimestampParser.parse(2303769600))
    print(TimestampParser.parse(2335305600))
    print(TimestampParser.parse(2366841600))
    print(TimestampParser.parse(2398464000))
    print(TimestampParser.parse(2429999999))