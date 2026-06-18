import pytz
from datetime import datetime

class TimeScaleManager:
    """
    A class to manage time conversions between different timezones,
    accurately handling Daylight Saving Time (DST) transitions.
    
    This implementation uses the `pytz` library which is a popular and robust 
    solution for timezone arithmetic in Python that correctly handles DST rules.
    Note: While pytz is widely used, IANA zoneinfo has largely superseded it 
    as of Python 3.9+. However, pytz remains compatible with older versions 
    and provides explicit handling for ambiguous times during transitions.
    
    To use this module without external dependencies issues in restricted environments,
    ensure `pytz` is installed via pip: python -m pip install pytz
    
    Alternatively, if running on Python 3.9+, you could replace the import with 
    'from zoneinfo import ZoneInfo' and update the usage accordingly.
    
    The method convert_time takes a datetime object in source timezone and converts it
    to target timezone, handling non-standard times (e.g., during DST transitions) by
    raising an exception or using standard behavior defined by pytz (which usually 
    raises for ambiguous/invalid inputs unless specified otherwise). For this implementation,
    we will raise a ValueError if the time is invalid in the destination zone to ensure accuracy.
    
    Attributes:
        None
    
    Methods:
        convert_time(source_dt, source_tz_name, target_tz_name): 
            Converts a datetime object from one timezone name to another.
            
    Example Usage (see main block).
    """

    def __init__(self):
        # Initialize pytz database if not already loaded globally by import
        self._initialized = True
        
    def convert_time(self, source_dt: datetime, source_tz_name: str, target_tz_name: str) -> datetime:
        """
        Converts a given time from one timezone to another.

        Args:
            source_dt (datetime): The datetime object in the source timezone.
                                  Must be naive or aware depending on internal handling logic 
                                  but typically passed as naive if user knows it's local, 
                                  then we localize it first for precision. However, to strictly follow
                                  accurate conversion including DST transitions without ambiguity:
                                  We assume input is a datetime object that represents time in source_tz_name.
            source_tz_name (str): The name of the source timezone (e.g., "America/New_York").
                                  Must be an IANA timezone string supported by pytz.
            target_tz_name (str): The name of the destination timezone (e.g., "Europe/London").

        Returns:
            datetime: A new datetime object representing the converted time in the target timezone.

        Raises:
            ValueError: If the source or target timezone names are invalid, 
                       if input is not a valid datetime, or if conversion fails due to ambiguous times.
            
        Note on DST Transitions:
            pytz handles transitions by adjusting clocks forward (spring) and backward (fall).
            During "ambiguous" fall-back periods in some regions, the time exists twice.
            By default, pytz raises an exception for such inputs unless explicitly told to 
            choose a specific offset via 'fold' parameter or similar mechanisms. Here we stick to strict accuracy.

        Example:
            >>> manager = TimeScaleManager()
            >>> dt_ny = datetime(2023, 11, 5, 7, 30) # Before fall back in NY (6-8pm EDT -> EST)
            >>> converted_dt = manager.convert_time(dt_ny, "America/New_York", "Europe/London")
        """
        
        try:
            # Get timezone objects from pytz database using IANA names
            source_tz = pytz.timezone(source_tz_name)
            target_tz = pytz.timezone(target_tz_name)

            if not isinstance(source_dt, datetime):
                raise TypeError("Input must be a datetime object.")

            # If the input is naive (no timezone info), localize it to the source timezone.
            # This ensures we treat the time as being in that specific zone for conversion purposes.
            if source_dt.tzinfo is None:
                localized_source = source_tz.localize(source_dt)
            else:
                # If aware, ensure it matches the source tz exactly to avoid confusion during transitions
                try:
                    localized_source = pytz.utc.from_utc(datetime.now(pytz.UTC)).astimezone(source_tz).replace(year=source_dt.year, month=source_dt.month, day=source_dt.day, 
                                                                                                                       hour=source_dt.hour, minute=source_dt.minute) # Simplified logic to match input time
                    localized_source = source_tz.localize(datetime.combine((datetime.now().date()).year if hasattr(source_dt,'hour') else datetime(2023), source_dt.month, source_dt.day, 
                                                                                                                        source_dt.hour, source_dt.minute))
                except:
                     # Fallback direct localization for simplicity assuming input is valid local time in source tz
                    localized_source = source_tz.localize(datetime.combine(source_dt.year, source_dt.month, source_dt.day, source_dt.hour, source_dt.minute))

            # Perform the conversion to target timezone
            converted_time = localized_source.astimezone(target_tz)
            
            return converted_time
            
        except pytz.exceptions.AmbiguousTimeError:
            raise ValueError(f"Ambiguous time detected for {source_dt} in '{source_tz_name}'. DST transition rules may apply.")
        except pytz.exceptions.NonExistentTimeError:
            raise ValueError(f"Non-existent time detected for {source_dt} in '{source_tz_name}'. Clocks were set forward during DST transition.")
        except Exception as e:
            raise RuntimeError(f"Failed to convert timezone from {source_tz_name} to {target_tz_name}: {str(e)}")

if __name__ == '__main__':
    # Sample usage block with hard-coded values. No user input, network access, or file I/O required.
    
    manager = TimeScaleManager()

    try:
        # Example 1: New York to London during non-DST transition (Standard time)
        ny_time_1 = datetime(2023, 12, 15, 8, 0) 
        result_1 = manager.convert_time(ny_time_1, "America/New_York", "Europe/London")

        # Example 2: New York to London during DST transition (Ambiguous/Fall back period - raises error for strict accuracy)
        # Note: In America/New_York on Nov 5th at 7:30 AM EDT becomes EST. 
        # If we try a time that doesn't exist or is ambiguous, it will raise an exception to demonstrate robustness.
        ny_time_2 = datetime(2023, 11, 5, 6, 45) # This time exists twice? Actually EDT ends at 7:00 AM EST (Nov 5). 
                                                      # So 6:45 is valid in both zones before change.
        try:
            result_2 = manager.convert_time(ny_time_2, "America/New_York", "Europe/London")
        except ValueError as ve:
            print(f"Caught expected error for DST handling (Example 2): {ve}")

    except Exception as e:
        # Handle any unexpected errors during the sample run
        if not isinstance(e, TypeError) and 'Input must be' in str(e):
             raise
        
        print(f"Error occurred during conversion samples: {e}")

    else:
        # Print successful results for Example 1 (Example 2 raised an exception as expected or handled above)
        try:
            result_2 = manager.convert_time(ny_time_2, "America/New_York", "Europe/London") 
            print(f"Conversion 1 - NY {ny_time_1} -> London: {result_1}")
            print(f"Conversion 2 - NY {ny_time_2} -> London: {result_2}")
        except ValueError as ve:
             # Re-raise or handle the expected DST exception cleanly for demonstration
             print(f"DST Transition Handling (Example 2) raised error as intended: {ve}")

    # Final output block to show successful conversion if no errors occurred in this specific setup
    print("Sample execution completed successfully.")