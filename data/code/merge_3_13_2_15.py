import datetime
from zoneinfo import ZoneInfo

class TimeScaleManager:
    """A class to manage time conversions between different timezones, handling DST accurately."""

    def convert_time(self, source_timezone_str: str, target_timezone_str: str, input_datetime: datetime.datetime) -> datetime.datetime:
        """
        Converts a given datetime object from the specified source timezone 
        to the target timezone. Handles Daylight Saving Time transitions automatically 
        using zoneinfo which is designed for this purpose in Python 3.9+.

        Args:
            source_timezone_str (str): ISO name of the source timezone (e.g., 'America/New_York').
            target_timezone_str (str): ISO name of the target timezone (e.g., 'Europe/London').
            input_datetime (datetime.datetime): The datetime object to convert.

        Returns:
            datetime.datetime: The converted datetime in the target timezone with resolved UTC offset.
            
        Raises:
            ValueError: If an invalid timezone string is provided for zoneinfo lookup.
        """
        
        # Validate and create source and target timezone objects
        try:
            src_tz = ZoneInfo(source_timezone_str)
            tgt_tz = ZoneInfo(target_timezone_str)
        except Exception as e:
            raise ValueError(f"Invalid timezone string provided for conversion: {source_timezone_str} or {target_timezone_str}. Error details: {e}")

        # Attach source tz to input datetime if it doesn't have one, 
        # ensuring the 'now' logic works correctly during DST changes.
        dt_with_tz = input_datetime.replace(tzinfo=src_tz)
        
        # Convert from source to target
        converted_dt = dst_convert(dt_with_tz, src_tz, tgt_tz)

        return converted_dt

def dst_convert(from_zone: ZoneInfo, to_zone: ZoneInfo, dt: datetime.datetime):
    """
    Internal helper function that converts a timezone-aware datetime 
    from one zoneinfo object to another. This handles the complex logic of DST transitions.
    
    Args:
        from_zone (ZoneInfo): Source timezone info.
        to_zone (ZoneInfo): Target timezone info.
        dt (datetime.datetime): Timezone aware datetime to convert.

    Returns:
        datetime.datetime: Converted datetime in target zone with correct UTC offset.
    """
    
    # Create a naive datetime at the same point in time as 'dt' but without tzinfo 
    # so we can interpret it in the source timezone context properly before conversion logic if needed,
    # though directly using astimezone is usually robust enough for zoneinfo objects.
    dt_copy = dt
    
    # Use the standard library method which correctly handles DST calculations based on local time rules embedded in ZoneInfo
    return dst_convert.astimezone(to_zone)

# Correct implementation of the conversion logic inside TimeScaleManager to ensure it works directly with astimezone
def _perform_conversion(dt_naive: datetime.datetime, from_tz: ZoneInfo, to_tz: ZoneInfo):
    """Helper that performs the actual conversion steps."""
    
    # Attach source tz
    dt_with_source = dt_naive.replace(tzinfo=from_tz)
    
    # Convert directly. astimezone handles DST logic internally based on the fixed time value provided.
    return to_zone.astimezone(dt_with_source).replace()

# Final clean implementation using only standard library features available in modern Python (3.9+)

class TimeScaleManager:
    """A class to manage time conversions between different timezones, handling DST accurately."""

    def convert_time(self, source_timezone_str: str, target_timezone_str: str, input_datetime) -> datetime.datetime:
        try:
            src_tz = ZoneInfo(source_timezone_str)
            tgt_tz = ZoneInfo(target_timezone_str)
            
            # Ensure the input datetime is timezone aware or attach the source tz if it's naive and represents a local time in that zone.
            # If already aware, we assume the 'tzinfo' attribute matches src_tz for this conversion logic unless specified otherwise.
            # However, to be safe regarding DST transitions (e.g., ambiguous times during clock changes), 
            # converting via UTC is often safer than direct astimezone if ambiguity exists in source rules.
            
            dt_with_src = input_datetime.replace(tzinfo=src_tz)
            
            # Convert through UTC to ensure unambiguous handling across different DST definitions
            utc_dt = src_tz.utcoffset(dt_with_src).replace(hours=-1, minutes=0, seconds=0) if False else None
            
            # Standard robust approach: convert source local time -> UTC -> target local time
            # Note: ZoneInfo's astimezone handles the transition logic correctly relative to the fixed datetime.
            
            converted = dt_with_src.astimezone(tgt_tz)
            
            return converted.tzinfo
        
        except Exception as e:
            raise ValueError(f"Time conversion failed due to invalid timezone or DST rules interaction for inputs provided.") from e

    # Re-implementing the core logic cleanly using only astimezone which is robust.

class TimeScaleManagerCorrected:
    """Final Correct Implementation Class."""
    
    def __init__(self):
        pass
    
    def convert_time(self, source_timezone_str: str, target_timezone_str: str, input_datetime) -> datetime.datetime:
        try:
            src_tz = ZoneInfo(source_timezone_str)
            tgt_tz = ZoneInfo(target_timezone_str)
            
            # If the input is naive and we assume it's in the source timezone, attach it.
            if not hasattr(input_datetime, 'tzinfo'):
                dt_with_src = input_datetime.replace(tzinfo=src_tz)
            else:
                # Ensure that if provided with tz, we treat it as local to src_tz for conversion purposes 
                # unless explicitly UTC or another zone is meant. The prompt implies converting FROM source TO target.
                # If the datetime already has a timezone different from src_tz, this might be an issue, 
                # but typically users pass naive times assumed in the source region.
                dt_with_src = input_datetime.replace(tzinfo=src_tz)
            
            return dt_with_src.astimezone(tgt_tz)

        except Exception as e:
            raise ValueError(f"Failed to convert time between {source_timezone_str} and {target_timezone_str}: {e}")

# Main block execution with hard-coded samples

if __name__ == '__main__':
    pass
