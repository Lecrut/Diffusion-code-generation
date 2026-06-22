class TimestampParser:
    SECONDS_IN_DAY = 86400
    EPOCH_YEAR = 1970
    DAYS_IN_MONTHS_COMMON = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    DAYS_IN_MONTHS_LEAP = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def days_in_year(year):
        return 366 if TimestampParser.is_leap_year(year) else 365

    @staticmethod
    def parse_timestamp_to_date(timestamp):
        if not isinstance(timestamp, int):
            raise ValueError("Timestamp must be an integer")
        if timestamp < 0:
            raise ValueError("Timestamp must be non-negative")
        
        total_days = timestamp // TimestampParser.SECONDS_IN_DAY
        year = TimestampParser.EPOCH_YEAR
        
        while True:
            days_in_current_year = TimestampParser.days_in_year(year)
            if total_days < days_in_current_year:
                break
            total_days -= days_in_current_year
            year += 1
            
        days_in_current_month = TimestampParser.DAYS_IN_MONTHS_LEAP if TimestampParser.is_leap_year(year) else TimestampParser.DAYS_IN_MONTHS_COMMON
        month = 1
        
        while month <= 12:
            if total_days < days_in_current_month[month - 1]:
                break
            total_days -= days_in_current_month[month - 1]
            month += 1
            
        day = total_days + 1
        return f"{year:04d}/{month:02d}/{day:02d}"

if __name__ == '__main__':
    sample_timestamps = [0, 86400, 1577836800, 1609459200]
    for ts in sample_timestamps:
        print(TimestampParser.parse_timestamp_to_date(ts))