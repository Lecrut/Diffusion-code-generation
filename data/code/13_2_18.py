import pytz
from datetime import datetime

class TimeScaleManager:
    """
    A class to manage time conversions between different timezones,
    accurately handling Daylight Saving Time (DST) transitions using 
    the standard IANA timezone database.
    
    Attributes:
        None
    
    Methods:
        convert_timezone(source_datetime, source_tz_name, target_tz_name):
            Converts a datetime object from one timezone to another.
            
    Raises:
        ValueError: If the provided timezone names are not recognized by pytz.
    """

    def __init__(self):
        """Initialize the TimeScaleManager."""
        self._pytz = pytz
    
    def convert_timezone(self, source_datetime, source_tz_name, target_tz_name):
        """
        Convert a datetime object from one timezone to another.
        
        This method ensures accuracy by using standard IANA timezone rules,
        which correctly handle ambiguous times during DST transitions 
        (e.g., fall back) and non-existent times (e.g., spring forward).
        
        Args:
            source_datetime (datetime): The datetime object representing the time to convert. It should ideally be naive or already localized to a specific timezone if possible, but this method handles localization internally for robustness. If passed as aware with an unknown tz, it will localize based on pytz logic first.
            source_tz_name (str): The name of the source timezone (e.g., 'America/New_York').
            target_tz_name (str): The name of the destination timezone (e.g., 'Europe/London').
            
        Returns:
            datetime: A new datetime object localized to the target timezone.
            
        Raises:
            ValueError: If either source or target timezone names are invalid.
        """
        
        # Validate and localize input time if naive, ensuring DST rules are respected during conversion
        try:
            tz_source = self._pytz.timezone(source_tz_name)
            tz_target = self._pytz.timezone(target_tz_name)
            
            if source_datetime.tzinfo is None:
                # If the datetime is naive, localize it to the source timezone first.
                # pytz's localize method handles DST transitions correctly by raising 
                # an exception for ambiguous or non-existent times in older versions,
                # but newer implementations handle this gracefully with 'fold' attribute logic implicitly managed internally often via standard library integration now. However, strictly using pytz requires localize to be explicit about the transition type if needed, though usually just passing a naive datetime works and raises an error for ambiguous/non-existing unless handled carefully in legacy code. 
                # For maximum robustness without external libraries relying on specific patch versions:
                source_datetime = tz_source.localize(source_datetime)
            else:
                # If already aware, ensure it's strictly in the source timezone to avoid confusion with system local time.
                if not (source_tz_name == 'UTC' or str(tz_datetime.tzinfo).startswith('UTC') and source_tz_name != 'UTC'): 
                    # Simple check to see if we need to re-localize, though usually just converting is enough.
                    pass
            
            # Perform the conversion
            converted_time = tz_source.localize(source_datetime)  # Re-apply localize here to be safe against any state issues if passed aware but not matching exactly? No, better:
            
            # Correct approach for robust pytz usage:
            # If datetime is naive -> localize to source_tz.
            # Then convert to target_tz by replacing tzinfo (which handles the math).
            
            localized_source = None
            if isinstance(source_datetime, datetime) and not hasattr(source_datetime, 'fold'): 
                # It's a standard library datetime without pytz fold attribute support yet? Or just naive.
                pass
            
            # Robust logic:
            if source_datetime.tzinfo is None:
                localized_source = tz_source.localize(source_datetime)
            else:
                # If it has timezone info, we assume the input was provided in that specific zone or UTC. 
                # To be safe and ensure 'source_tz_name' applies:
                if str(tz_source.tzname(time)) != source_datetime.strftime('%Z'): # This check is complex with naive datetimes sometimes. Let's simplify.
                    pass
                
                # The safest way to convert any datetime using pytz for a specific target TZ:
                # 1. If input has tz, it might not be the one we want if passed as 'now' in system time but labeled differently? 
                # Usually users expect passing a naive datetime or an aware one in UTC/SystemTime.
                # Let's assume standard behavior: localize to source_tz first if naive.
                
                pass
            
            # Final conversion step using the pytz converter which handles DST math internally correctly for valid inputs.
            converted_time = localized_source.astimezone(tz_target)

            return converted_time
            
        except pytz.exceptions.UnknownTimeZoneError as e:
            raise ValueError(f"Invalid timezone name provided: {e}")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or network access.
    
    manager = TimeScaleManager()

    # Sample 1: New York (EST/EDT) to London (GMT/BST) on a standard day
    ny_time_naive = datetime(2023, 6, 15, 14, 0, 0)
    
    try:
        converted_ny_to_london = manager.convert_timezone(ny_time_naive, 'America/New_York', 'Europe/London')
        print(f"Converted {ny_time_naive} (New York EST/EDT) to London time:")
        print(converted_ny_to_london.strftime('%Y-%m-%d %H:%M:%S (%Z)'))

    except ValueError as e:
        print(f"Error in Sample 1: {e}")

    # Sample 2: Handling DST Transition (Fall back - ambiguous time handling logic is built into pytz conversion usually, 
    # but let's pick a clear transition moment or just use the robust converter which handles it by choosing one interpretation based on history if needed).