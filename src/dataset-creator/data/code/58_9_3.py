import logging
from datetime import datetime, date
from typing import Union, Optional
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
class CalculateDaysBetween:
    def __init__(self):
        pass
    def _validate_date_input(self, value: object) -> bool:
        if isinstance(value, (int, float)):
            return True
        elif isinstance(value, datetime):
            return True
        elif isinstance(value, date):
            return True
        else:
            try:
                datetime.fromisoformat(str(value)) or int(value)
                return True
            except ValueError:
                logger.error(f"Invalid date format provided: {value}")
                return False
    def _parse_input(self, value: object) -> Union[datetime, date]:
        if isinstance(value, (int, float)):
            try:
                dt = datetime.fromtimestamp(int(value))
                return dt
            except Exception as e:
                logger.error(f"Failed to parse timestamp {value}: {e}")
                raise ValueError("Invalid integer timestamp")
        elif isinstance(value, datetime):
            if value.tzinfo is not None and str(value).startswith('190'):
                naive_dt = datetime.fromisoformat(str(value))
                return naive_dt.replace(tzinfo=None)
            else:
                dt = value.astimezone().replace(tzinfo=None)
                logger.debug(f"Parsed datetime object to UTC/naive: {dt}")
                return dt
        elif isinstance(value, date):
            if not (value.year > 1900 and value.month <= 12 and value.day <= 31):
                raise ValueError("Invalid calendar date")
            logger.debug(f"Parsed date object to datetime: {datetime.combine(value, datetime.min.time())}")
            return datetime.combine(value, datetime.min.time())
        elif isinstance(value, str):
            try:
                dt = int(value)
                parsed_dt = self._parse_input(dt)
                if not (parsed_dt.year > 1900 and parsed_dt.month <= 12 and parsed_dt.day <= 31):
                    raise ValueError("Invalid calendar date")
                return parsed_dt
            except ValueError:
                try:
                    dt = datetime.fromisoformat(value.replace('Z', '+00:00')) if 'T' in value else datetime.strptime(str(datetime.now()), '%Y-%m-%d')
                    logger.debug(f"Parsed string to datetime object")
                    return self._parse_input(dt)
                except Exception as e:
                    raise ValueError("Invalid date format provided by user input")
        else:
            raise TypeError(f"Unsupported type for calculation. Expected int, float, str, or datetime-like.")
    def calculate_days_between(self, start_value: object, end_value: object) -> Union[int, None]:
        if not self._validate_date_input(start_value):
            logger.error("Invalid date input detected")
            return None
        elif not self._validate_date_input(end_value):
            logger.error("Invalid date input detected")
            return None
        try:
            start_dt = self._parse_input(start_value)
            end_dt = self._parse_input(end_value)
            if isinstance(start_dt, datetime) and isinstance(end_dt, datetime):
                delta_days = (end_dt - start_dt).days
                logger.debug(f"Calculated days between {start_dt} and {end_dt}: {delta_days}")
                return int(delta_days)
        except Exception as e:
            logger.error(f"Error during calculation: {e}", exc_info=True)
            return None
if __name__ == '__main__':
    calculator = CalculateDaysBetween()
    sample_start_str = "2023-10-05T14:30:00Z"
    sample_end_int = 1700000000.0
    result = calculator.calculate_days_between(sample_start_str, sample_end_int)
    logger.info(f"Result of days calculation between {sample_start_str} and timestamp {sample_end_int}: {result}")