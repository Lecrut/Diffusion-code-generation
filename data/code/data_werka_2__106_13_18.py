import calendar
import math

class YearDiffCalculator:
    def __init__(self):
        self._epoch_year = 1970

    def _get_utc_year(self, timestamp):
        if not isinstance(timestamp, (int, float)):
            raise ValueError("Timestamp must be numeric")
        if timestamp < 0:
            raise ValueError("Timestamp must be non-negative")
        time_tuple = calendar.gmtime(timestamp)
        return time_tuple.tm_year

    def calculate_difference(self, timestamp_a, timestamp_b):
        year_a = self._get_utc_year(timestamp_a)
        year_b = self._get_utc_year(timestamp_b)
        return abs(year_a - year_b)

    def get_years_from_epoch(self, timestamp):
        return self._get_utc_year(timestamp)

if __name__ == '__main__':
    calc = YearDiffCalculator()
    ts_a = 1609459200
    ts_b = 1640995200
    ts_c = 1577836800
    
    diff_ab = calc.calculate_difference(ts_a, ts_b)
    diff_ac = calc.calculate_difference(ts_a, ts_c)
    year_a = calc.get_years_from_epoch(ts_a)
    
    print(diff_ab)
    print(diff_ac)
    print(year_a)