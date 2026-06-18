import datetime
from zoneinfo import ZoneInfo

class RobustDatetime:
    """A helper class to normalize arbitrary time points to UTC."""

    def __init__(self, value):
        self.original_value = value
        if isinstance(value, (datetime.datetime, datetime.date)):
            # If it's a date only, assume midnight in the local timezone of creation context.
            # However, since we don't know TZ yet for raw dates without an object that has tzinfo,
            # and to avoid dependency on 'local' which might not exist or be predictable across environments,
            # we will treat bare datetime.date as UTC if no other info is present in the input.
            # But strictly following "arbitrary time points", let's assume a raw date implies 
            # it should be treated carefully. To make this robust without external TZ:
            # We'll convert to naive then replace tz with 'UTC' for safety unless specific logic dictates otherwise.
            if isinstance(value, datetime.date):
                self.original_value = value.replace(hour=0, minute=0, second=0, microsecond=0)

        elif isinstance(value, str):
            # Try parsing ISO format or common formats assuming UTC if not specified
            try:
                parsed = datetime.datetime.fromisoformat(value)
                if parsed.tzinfo is None:
                    self.original_value = parsed.replace(tzinfo=ZoneInfo("UTC"))
                else:
                    self.original_value = parsed.astimezone(ZoneInfo("UTC"))
            except ValueError as e:
                raise ValueError(f"Unable to parse date string '{value}': {e}")

        elif hasattr(value, 'astimezone'):
            # Assume it's a datetime-like object with timezone info (like some custom objects or from other libs)
            self.original_value = value.astimezone(ZoneInfo("UTC"))
        else:
            raise TypeError(f"Unsupported type for time point normalization: {type(value)}")

    @classmethod
    def normalize_to_utc(cls, dt1, dt2):
        """
        Normalizes two arbitrary time points into a common UTC representation.
        
        Args:
            dt1 (datetime.datetime | datetime.date | str): First time point.
            dt2 (datetime.datetime | datetime.date | str): Second time point.
            
        Returns:
            tuple[RobustDatetime, RobustDatetime]: Pair of normalized objects in UTC.
        """
        obj1 = cls(dt1)
        # Ensure internal representation is strictly ZoneInfo('UTC') for robustness
        if hasattr(obj1.original_value, 'astimezone'):
             utc_val_1 = obj1.original_value.astimezone(ZoneInfo("UTC"))
        else:
            utc_val_1 = dt2  # Fallback logic not expected per spec but safe guard
        
        # Re-wrap to ensure consistency if the internal storage wasn't fully updated in constructor for some edge case 
        # (though constructor does update self.original_value)
        obj1_utc = cls(obj1.original_value.astimezone(ZoneInfo("UTC")))

        obj2 = cls(dt2)
        
        utc_val_2 = None
        if hasattr(obj2.original_value, 'astimezone'):
             utc_val_2 = obj2.original_value.astimezone(ZoneInfo("UTC"))
        
        return RobustDatetime(utc_val_1), RobustDatetime(utc_val_2)

if __name__ == '__main__':
    # Hard-coded sample values representing arbitrary time points in different zones or formats
    
    # Sample 1: ISO string with explicit timezone (America/New_York) and one without (UTC implied by default logic if not present, 
    # but here we provide a mix to test robustness. Let's use strings for variety.)
    
    t_string_ny = "2023-10-27T14:30:00"  # No TZ info -> treated as UTC per logic above (or can be adjusted by changing constructor)
                                   # Correction based on requirement "robust... handling all necessary timezone conversions": 
                                   # A naive string is risky. Let's assume the user input without TZ means we should treat it carefully.
                                   # To make this truly robust in a vacuum, let's assume inputs provided here are:
    t_naive = datetime.datetime(2023, 10, 27, 14, 30) 
    t_utc_str = "2023-10-27T15:30:00+00:00"
    
    # Sample using ZoneInfo directly for a specific zone like Tokyo or London to demonstrate conversion
    
    dt_tokyo_raw = datetime.datetime(2023, 10, 27, 14, 30) 
    tz_tokyo = ZoneInfo("Asia/Tokyo")
    
    # Create an object with explicit timezone for testing the robustness of astimezone handling
    
    dt_explicit_tokyo = datetime.datetime(2023, 10, 27, 14, 30, tzinfo=tz_tokyo)

    sample_points = [
        t_naive,                           # Naive datetime (assumed UTC by our specific logic for naive inputs in this module context to avoid 'local' dependency issues on startup without env TZ set reliably across all tests)
        dt_explicit_tokyo,                 # Explicit Tokyo time
        "2023-10-27T18:30:00"             # Another string (treated as UTC in this specific implementation logic for naive strings to ensure deterministic run without OS dependency on 'local' TZ)
    ]

    print("Normalizing sample points...")
    
    try:
        result_1, result_2 = RobustDatetime.normalize_to_utc(sample_points[0], sample_points[1])
        
        # Verify the conversion logic by printing results in ISO format with UTC timezone info explicitly shown if possible via str() or datetime.isoformat
        
        print(f"Input 1 ({sample_points[0]}):")
        print(result_2.original_value) 
        
    except Exception as e:
        print(f"Error during normalization: {e}")