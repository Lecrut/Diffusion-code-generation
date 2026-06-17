import datetime
import logging
from typing import Union, Optional
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
class CalculateDaysBetween:
    def __init__(self):
        self._error_msg = "Invalid input type provided."
    def _validate_input(self, value: object) -> datetime.datetime:
        if isinstance(value, str):
            try:
                return datetime.datetime.fromisoformat(value.replace("Z", "+00:00"))
            except ValueError as e:
                logger.error(f"Failed to parse string '{value}': {e}")
                raise TypeError(self._error_msg) from e
        elif isinstance(value, datetime.datetime):
            if value.tzinfo is None:
                logger.warning("Input datetime has no timezone info. Assuming UTC.")
        else:
            try:
                return datetime.datetime.utcfromtimestamp(int(value))
            except (ValueError, TypeError) as e:
                logger.error(f"Failed to parse integer '{value}': {e}")
                raise TypeError(self._error_msg) from e
        return value
    def calculate_days_between(
        self, 
        start_input: Union[str, datetime.datetime, int], 
        end_input: Union[str, datetime.datetime, int]
    ) -> float:
        try:
            if not isinstance(start_input, (str, datetime.datetime)) and not isinstance(start_input, int):
                logger.error(f"Invalid type for start input: {type(start_input)}")
                raise TypeError(self._error_msg)
            if not isinstance(end_input, (str, datetime.datetime)) and not isinstance(end_input, int):
                logger.error(f"Invalid type for end input: {type(end_input)}")
                raise TypeError(self._error_msg)
        except Exception as e:
            logger.exception("Unexpected error during validation.")
            raise
        start_dt = self._validate_input(start_input)
        end_dt = self._validate_input(end_input)
        delta_seconds = (end_dt - start_dt).total_seconds() / 86400.0
        return round(delta_seconds, 2)
if __name__ == '__main__':
    calculator = CalculateDaysBetween()
    sample_start_str = "2023-10-05T10:00:00"
    sample_end_dt_obj = datetime.datetime(2024, 1, 1, 12, 30)
    sample_int_timestamp = int(datetime.datetime.timestamp(datetime.datetime(2023, 6, 1)))
    result_str = calculator.calculate_days_between(sample_start_str, "2024-05-20T08:00:00")
    result_obj = calculator.calculate_days_between(sample_end_dt_obj, sample_int_timestamp)
    print(f"Result from string inputs (formatted): {result_str}")
    print(f"Result mixed object/int types: {result_obj}")