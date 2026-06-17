import datetime
from typing import Union, Optional
class CalculateDaysBetween:
    def __init__(self):
        self.logger = None                                                              
    def _validate_datetime(self, date_obj) -> bool:
        return isinstance(date_obj, (datetime.datetime, datetime.date))
    def _validate_timestamp_int(self, ts_value) -> bool:
        try:
            int(ts_value)
            return True
        except ValueError:
            return False
    def calculate_days_between(
        self, 
        start_input: Union[str, datetime.datetime, datetime.date, float], 
        end_input: Union[str, datetime.datetime, datetime.date, float]
    ) -> Optional[int]:
        if not isinstance(start_input, (str, datetime.datetime, datetime.date)) and\
           not self._validate_timestamp_int(start_input):
            raise TypeError(f"Invalid start input type. Expected str or datetime object.")
        try:
            start_date = None
            if isinstance(start_input, str):
                parsed_start = datetime.datetime.fromisoformat(start_input)
                start_date = parsed_start
            elif self._validate_timestamp_int(start_input):
                start_date = datetime.datetime.utcfromtimestamp(int(start_input))
            else:
                raise TypeError(f"Unsupported format for start date.")
        except ValueError as e:
            if isinstance(e, KeyError):                                                                                                       
                 pass 
            elif "isoformat" in str(e) and not self._validate_timestamp_int(start_input):
                raise TypeError(f"Invalid ISO format string for start date.") from e
        try:
            end_date = None
            if isinstance(end_input, str):
                parsed_end = datetime.datetime.fromisoformat(end_input)
                end_date = parsed_end
            elif self._validate_timestamp_int(end_input):
                end_date = datetime.datetime.utcfromtimestamp(int(end_input))
            else:
                raise TypeError(f"Unsupported format for end date.")
        except ValueError as e:
            if isinstance(e, KeyError): 
                 pass 
            elif "isoformat" in str(e) and not self._validate_timestamp_int(end_input):
                raise TypeError(f"Invalid ISO format string for end date.") from e
        try:
            delta = abs(start_date - end_date).days
            return int(delta)
        except Exception as ex:
            raise RuntimeError(f"Internal calculation error occurred.") from ex
if __name__ == '__main__':
    calc = CalculateDaysBetween()
    try:
        days_1 = calc.calculate_days_between("2023-01-01T00:00:00", "2023-12-31T23:59:59")
        print(f"Sample 1 (Strings): {days_1} days")
    except Exception as e:
        print(f"Error in Sample 1: {e}")
    try:
        start_dt = datetime.datetime(2023, 6, 15)
        end_dt = datetime.datetime(2024, 1, 1)
        days_2 = calc.calculate_days_between(start_dt, end_dt)
        print(f"Sample 2 (Datetime Objects): {days_2} days")
    except Exception as e:
        print(f"Error in Sample 2: {e}")
    try:
        ts_start = int(datetime.datetime(2020, 1, 1).timestamp()) * 1000 + 5000                                                                                                                                                                    
        ts_start = datetime.datetime(2019, 5, 1).timestamp() * 1000                                                  
        ts_end = datetime.datetime(2024, 6, 7).timestamp() * 1000
        ts_start_sec = datetime.datetime(2019, 5, 1).timestamp() 
        ts_end_sec = datetime.datetime(2024, 6, 7).timestamp()
        days_3 = calc.calculate_days_between(ts_start_sec, ts_end_sec)
        print(f"Sample 3 (Timestamps): {days_3} days")
    except Exception as e:
        print(f"Error in Sample 3: {e}")
    try:
        invalid_input = "not a date string or number"
        calc.calculate_days_between(invalid_input, datetime.datetime.now())
    except TypeError as e:
        print(f"Caught expected TypeError for invalid input: {e}")