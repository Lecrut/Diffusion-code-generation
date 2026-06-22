class TimestampParser:
    DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    SECONDS_PER_DAY = 86400
    EPOCH_YEAR = 1970

    @staticmethod
    def _is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @staticmethod
    def _get_days_in_year(year):
        return 366 if TimestampParser._is_leap_year(year) else 365

    def parse(self, timestamp):
        if not isinstance(timestamp, int):
            raise ValueError("Timestamp must be an integer")
        if timestamp < 0:
            raise ValueError("Timestamp must be non-negative")
        
        days = timestamp // self.SECONDS_PER_DAY
        year = self.EPOCH_YEAR
        
        while True:
            days_in_year = self._get_days_in_year(year)
            if days < days_in_year:
                break
            days -= days_in_year
            year += 1
        
        month_days = list(self.DAYS_IN_MONTH)
        if self._is_leap_year(year):
            month_days[1] = 29
            
        month = 1
        while month <= 12:
            if days < month_days[month - 1]:
                break
            days -= month_days[month - 1]
            month += 1
            
        day = days + 1
        return f"{year:04d}/{month:02d}/{day:02d}"

if __name__ == '__main__':
    parser = TimestampParser()
    samples = [0, 86400, 1609459200, 1704067200]
    for ts in samples:
        print(parser.parse(ts))