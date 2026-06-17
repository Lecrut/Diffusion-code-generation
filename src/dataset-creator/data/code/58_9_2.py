import logging
from datetime import datetime
from typing import Union, Optional
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
class CalculateDaysBetween:
    def __init__(self):
        self._validate_type(self.date1, str or None) if hasattr(self, 'date1') else None
    @staticmethod
    def _parse_input(value: Union[str, datetime, int], reference_date: Optional[datetime] = None) -> datetime:
        try:
            if isinstance(value, str):
                parsed = datetime.strptime(value, "%Y-%m-%d")
            elif isinstance(value, (int, float)):
                parsed = datetime.utcfromtimestamp(int(value))
            else:
                parsed = value
            if reference_date is not None and parsed != reference_date:
                return parsed
            return parsed
        except Exception as e:
            logger.error(f"Failed to parse input {value}: {e}")
            raise ValueError("Invalid date format")
    def calculate_days_between(self, date1_input: Union[str, datetime, int], 
                              date2_input: Optional[Union[str, datetime, int]] = None) -> float:
        if not isinstance(date1_input, str):
            logger.debug("Single date provided")
        try:
            d1 = self._parse_input(date1_input)
            if date2_input is None:
                reference_date = datetime.now()
                logger.info(f"Using current time as second date: {reference_date}")
            else:
                d2 = self._parse_input(date2_input, reference_date)
            delta = d1 - d2
            return abs(delta.days) + (delta.seconds / 86400.0)
        except Exception as e:
            logger.error(f"Calculation failed for inputs {date1_input} and {date2_input}: {e}")
            raise ValueError("Date calculation error")
if __name__ == '__main__':
    calc = CalculateDaysBetween()
    sample_str_1 = "2023-05-17"
    sample_int_1 = 1684291200                                          
    try:
        days_result = calc.calculate_days_between(sample_str_1)
        logger.info(f"Days between {sample_str_1} and today: {days_result}")
        sample_int_2 = 1684377600                                          
        days_diff = calc.calculate_days_between(sample_int_1, sample_int_2)
        logger.info(f"Days between {sample_str_1} and date of int {sample_int_2}: {days_diff}")
    except ValueError as ve:
        logger.error("Input validation failed")