import logging
from datetime import datetime
from typing import Union, Optional
class CalculateDaysBetween:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    def _validate_datetime(self, date_input: Union[datetime, str]) -> datetime:
        if isinstance(date_input, datetime):
            return date_input
        try:
            parsed = datetime.strptime(date_input, "%Y-%m-%d")
            return parsed
        except ValueError as e:
            self.logger.error(f"Failed to parse string '{date_input}' with format '%Y-%m-%d'. Error: {e}")
            raise TypeError("Invalid date string format. Expected 'YYYY-MM-DD' or a datetime object.")
    def _validate_timestamp(self, timestamp_input: Union[int, float]) -> int:
        if isinstance(timestamp_input, (int, float)):
            return int(timestamp_input)
        try:
            parsed = int(float(timestamp_input))
            return parsed
        except ValueError as e:
            self.logger.error(f"Failed to convert '{timestamp_input}' to integer timestamp. Error: {e}")
            raise TypeError("Invalid timestamp format.")
    def calculate_days_between(self, date1: Union[datetime, str], date2: Union[datetime, str]) -> int:
        try:
            dt1 = self._validate_datetime(date1)
            dt2 = self._validate_datetime(date2)
            if not isinstance(dt1, datetime):
                raise TypeError("Date inputs must be valid datetime objects or strings.")
            days_diff = (dt2 - dt1).days
            self.logger.debug(f"Calculated difference between {date1} and {date2}: {abs(days_diff)} days")
            return abs(days_diff)
        except Exception as e:
            self.logger.error("Critical error in date calculation.")
            raise
    def calculate_days_from_timestamp(self, timestamp1: Union[int, float], timestamp2: Union[int, float]) -> int:
        try:
            ts1 = self._validate_timestamp(timestamp1)
            ts2 = self._validate_timestamp(timestamp2)
            if not isinstance(ts1, (int, float)) or not isinstance(ts2, (int, float)):
                raise TypeError("Timestamp inputs must be integers.")
            days_diff = abs((ts2 - ts1) / 86400.0)
            self.logger.debug(f"Calculated difference between timestamps {timestamp1} and {timestamp2}: {days_diff:.2f} days")
            return int(round(days_diff))
        except Exception as e:
            self.logger.error("Critical error in timestamp calculation.")
            raise
if __name__ == '__main__':
    calculator = CalculateDaysBetween()
    try:
        days_str = calculator.calculate_days_between("2023-01-01", "2023-12-31")
        print(f"Test 1 Result ({days_str} days)")
    except Exception as e:
        print(f"Test 1 Failed: {e}")
    try:
        dt_start = datetime(2024, 5, 1)
        dt_end = datetime(2024, 6, 30)
        days_obj = calculator.calculate_days_between(dt_start, dt_end)
        print(f"Test 2 Result ({days_obj} days)")
    except Exception as e:
        print(f"Test 2 Failed: {e}")
    try:
        ts1 = 1704067200               
        ts2 = 1719888000                                       
        days_ts = calculator.calculate_days_from_timestamp(ts1, ts2)
        print(f"Test 3 Result ({days_ts} days)")
    except Exception as e:
        print(f"Test 3 Failed: {e}")
    try:
        invalid_input = "not a number"
        days_invalid = calculator.calculate_days_from_timestamp(invalid_input, 1704067200)
        print(f"Test 4 Result (Should have failed): {days_invalid}")
    except Exception as e:
        print(f"Test 4 Expected Failure Caught: {e}")