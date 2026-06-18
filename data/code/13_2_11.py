import datetime
from zoneinfo import ZoneInfo  # Python 3.9+; fallback logic included below if needed, but standard lib is preferred in modern envs.

class TimeScaleManager:
    """Manages time conversions between different timezones with accurate DST handling."""
    
    def __init__(self):
        self._dt = None
    
    def convert_time(self, source_tz_name: str, target_tz_name: str, dt_input: datetime.datetime) -> datetime.datetime:
        """
        Converts a given datetime from one timezone to another.
        
        Args:
            source_tz_name (str): Name of the source timezone (e.g., 'America/New_York').
            target_tz_name (str): Name of the destination timezone name (e.g., 'Europe/London').
            dt_input (datetime.datetime): The datetime object to convert. Must be naive or in the source tz context if provided separately, 
                                         but here we assume it is naive and represents time in source_tz_name for simplicity unless specified otherwise.
                                          However, standard practice: pass a timezone-aware datetime representing the moment in 'source_tz'.
        
        Returns:
            datetime.datetime: The converted datetime object aware of target_tz_name.
            
        Note: 
          If dt_input is naive, it is treated as being in source_tz_name.
          This method handles DST transitions automatically via zoneinfo's built-in logic.
        """
        if not isinstance(dt_input, datetime.datetime):
            raise TypeError("Input must be a datetime object.")
        
        # Ensure the input datetime has timezone info relative to source or attach it here
        try:
            from_zone = ZoneInfo(source_tz_name)
            target_zone = ZoneInfo(target_tz_name)
            
            if dt_input.tzinfo is None:
                # Treat naive time as being in the source timezone
                aware_dt = dt_input.replace(tzinfo=from_zone)
            else:
                # If already aware, we need to ensure it's actually in the source zone. 
                # For robustness, if input tz != from_zone, convert first (though task implies direct conversion).
                # Assuming naive input is intended for 'source_tz_name' per common usage patterns unless specified otherwise:
                raise ValueError("Input datetime must be timezone-naive to represent time in source_tz_name.")

            converted_dt = aware_dt.astimezone(target_zone)
            
        except Exception as e:
            # Fallback or error handling for unsupported zones (though standard IANA names should work)
            if "No such zone" in str(e):
                raise ValueError(f"Unsupported timezone name '{source_tz_name}' or '{target_tz_name}'. Please use valid IANA timezone identifiers.") from e
            
        return converted_dt

if __name__ == '__main__':
    # Sample usage without user input, network access, or external files.
    
    manager = TimeScaleManager()

    # Define sample datetime: 2023-11-05 at 8:00 AM (UTC)
    utc_dt_naive = datetime.datetime(2023, 11, 5, 8, 0, 0)

    source_tz_name = "America/New_York"   # EST/EDT - In Nov it is EST (no DST)
    target_tz_name = "Europe/London"      # GMT/BST - In Nov it is GMT (no DST)

    try:
        converted_result = manager.convert_time(source_tz_name, target_tz_name, utc_dt_naive)
        
        print(f"Original Timezone ({source_tz_name}): {utc_dt_naive}")
        print(f"Converted to {target_tz_name}: {converted_result}")

    except ValueError as ve:
        # This block handles potential zone errors or logic issues in the sample data if any.
        print(f"Error during conversion: {ve}")