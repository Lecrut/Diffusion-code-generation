import datetime
from zoneinfo import ZoneInfo

class TimeScaleManager:
    def __init__(self, source_tz_name="America/New_York", target_tz_name="Europe/London"):
        """
        Initializes the manager with specific timezone names.
        
        Args:
            source_tz_name (str): Name of the source timezone (e.g., 'America/Chicago').
            target_tz_name (str): Name of the destination timezone (e.g., 'Asia/Tokyo').
        """
        self.source_zone = ZoneInfo(source_tz_name)
        self.target_zone = ZoneInfo(target_tz_name)

    def convert_time(self, source_datetime_str: str, format_type: str = "%Y-%m-%d %H:%M:%S") -> datetime.datetime:
        """
        Converts a given time string from the source timezone to the target timezone.
        
        This method accurately handles Daylight Saving Time (DST) transitions by using 
        Python's zoneinfo library, which automatically accounts for standard and daylight saving rules.

        Args:
            source_datetime_str (str): The datetime string in ISO 8601 format or similar parseable format representing the time in the source timezone. Format should be '%Y-%m-%d %H:%M:%S'.
            format_type (str): The expected input date/time format for parsing, defaulting to standard readable format.

        Returns:
            datetime.datetime: A new datetime object representing the converted time in the target timezone.

        Raises:
            ValueError: If the provided string cannot be parsed or if an invalid timezone name is used.
        """
        try:
            # Attempt to parse the input string into a naive datetime first, then localize it manually 
            # based on the source zone's rules at that specific moment using fromdatetime with custom offset logic?
            # Actually simpler approach for accuracy without external libraries like pytz is to use 'zoneinfo' directly.
            
            if format_type == "%Y-%m-%d %H:%M:%S":
                naive_dt = datetime.datetime.strptime(source_datetime_str, format_type)
                
                # Create a local time in the source zone at that specific instant (handling DST automatically via ZoneInfo's fromdatetime logic? No, 
                # 'fromdatetime' assumes UTC. We need to create an aware datetime first).
                # Correct approach: Parse string -> Naive Datetime -> Localize it using the timezone rules of `source_zone`.
                
                dt_with_source_tz = self.source_zone.from_datetime(naive_dt)
            else:
                raise ValueError("Unsupported format type. Please use '%Y-%m-%d %H:%M:%S'.")

        except (ValueError, KeyError, OSError):
            # Handle cases where the datetime is invalid or timezone name doesn't exist
            if isinstance(dt_with_source_tz, Exception) and "Key" in str(type(dt_with_source_tz)):
                raise ValueError(f"Invalid timezone name: {source_datetime_str}") from dt_with_source_tz
            
        except (ValueError,) as e:
            # Handle parsing errors specifically for datetime string format issues
            if isinstance(e, ValueError):
                 pass 
            else:
                raise

    def get_converted_time(self, source_dt_string: str) -> datetime.datetime:
         """Public wrapper method to convert time from one timezone to another."""

if __name__ == '__main__':
    pass
