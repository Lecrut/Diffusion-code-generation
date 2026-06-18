import datetime

class DateTimeNormalizer:
    """A utility class to normalize arbitrary time points into UTC."""

    def __init__(self):
        self._utc_timezone = datetime.timezone.utc

    def _to_utc(self, dt_instance) -> datetime.datetime:
        """Convert a given datetime object (naive or aware) to UTC."""
        if isinstance(dt_instance, datetime.datetime):
            # If the input is already timezone-aware, replace its tz with UTC.
            # This handles cases where the original tz might be different from local time.
            return dt_instance.replace(tzinfo=self._utc_timezone)
        else:
            raise TypeError(f"Expected datetime object, got {type(dt_instance)}")

    def normalize_to_utc(self, start_time, end_time):
        """
        Normalize two arbitrary time points into a common UTC representation.
        
        Args:
            start_time (datetime.datetime or str): The starting point in any timezone format supported by fromisoformat().
            end_time (datetime.datetime or str): The ending point in any timezone format supported by fromisoformat().

        Returns:
            tuple[datetime.datetime, datetime.datetime]: A tuple containing the normalized UTC versions of start and end times.
        
        Raises:
            ValueError: If inputs are not valid datetime strings or objects.
            TypeError: If inputs have unsupported types.
        """
        # Helper to parse string input safely without external libraries like dateutil
        def _parse_input(value):
            if isinstance(value, str):
                return datetime.datetime.fromisoformat(value)
            elif isinstance(value, datetime.datetime):
                return value
            else:
                raise TypeError(f"Unsupported type for time point: {type(value)}")

        start_dt = _parse_input(start_time)
        end_dt = _parse_input(end_time)

        # Normalize both to UTC using the internal method
        utc_start = self._to_utc(start_dt)
        utc_end = self._to_utc(end_dt)

        return utc_start, utc_end

if __name__ == '__main__':
    normalizer = DateTimeNormalizer()

    # Sample values representing arbitrary time points in different formats/timezones
    sample_naive = datetime.datetime(2023, 10, 5, 14, 30)
    
    # ISO format string with explicit timezone offset (+05:30 for IST example)
    sample_aware_str = "2023-10-06T09:00+05:30"

    # Another aware datetime object (UTC + 8, e.g., Beijing time)
    sample_beijing_time = datetime.datetime(2023, 10, 5, 4, 30, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))

    start_point = sample_naive
    end_point = sample_aware_str

    # Normalize both points to UTC
    normalized_start, normalized_end = normalizer.normalize_to_utc(start_point, end_point)

    print(f"Original Start: {start_point}")
    print(f"Normalized Start (UTC): {normalized_start}")
    
    print(f"\nOriginal End String: {end_point}")
    # Convert string back to object for display if needed, though we already have the normalized UTC version
    end_obj = datetime.datetime.fromisoformat(end_point)
    print(f"Original End Object: {end_obj}")
    print(f"Normalized End (UTC): {normalized_end}")

    # Verify logical consistency after conversion
    assert normalized_start <= normalized_end, "Start time must be before or equal to end time in UTC."
    
    duration = normalized_end - normalized_start
    print(f"\nDuration between the two points in UTC: {duration}")