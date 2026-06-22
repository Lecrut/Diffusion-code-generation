class EpochDayExtractor:
    SECONDS_PER_DAY = 86400
    DAYS_IN_MONTHS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    @staticmethod
    def _is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @staticmethod
    def get_day_from_epoch(timestamp):
        if not isinstance(timestamp, int):
            raise ValueError("Timestamp must be an integer")
        if timestamp < 0:
            raise ValueError("Timestamp must be non-negative")
        
        days_since_epoch = timestamp // EpochDayExtractor.SECONDS_PER_DAY
        
        current_year = 1970
        while True:
            days_in_current_year = 366 if EpochDayExtractor._is_leap_year(current_year) else 365
            if days_since_epoch < days_in_current_year:
                break
            days_since_epoch -= days_in_current_year
            current_year += 1
        
        is_leap = EpochDayExtractor._is_leap_year(current_year)
        months_days = EpochDayExtractor.DAYS_IN_MONTHS
        if is_leap:
            months_days = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        
        month = 0
        while month < 12:
            if days_since_epoch < months_days[month]:
                break
            days_since_epoch -= months_days[month]
            month += 1
        
        day = days_since_epoch + 1
        return day

if __name__ == '__main__':
    extractor = EpochDayExtractor()
    sample_timestamp = 1609459200
    result = extractor.get_day_from_epoch(sample_timestamp)
    print(result)