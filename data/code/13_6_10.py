import re

def parse_timezone_config(content):
    """Parses a configuration string containing two time zone definitions."""
    # Pattern to match lines like "timezone: UTC" or "zone: America/New_York"
    pattern = r'(?:timezone|zone)\s*:\s*(\S+)'
    
    matches = re.findall(pattern, content)
    
    if len(matches) != 2:
        raise ValueError("Configuration must contain exactly two time zone definitions.")
    
    return [matches[0], matches[1]]

def calculate_hour_difference(zone_name_1, zone_name_2):
    """Calculates the difference in hours between two IANA timezone strings."""
    # Using pytz for standard timezone handling (no external network calls needed if installed)
    try:
        import pytz
    except ImportError:
        raise RuntimeError("pytz is required. Install it via 'pip install pytz'.")

    tz1 = pytz.timezone(zone_name_1)
    tz2 = pytz.timezone(zone_name_2)

    # Create a reference datetime (e.g., UTC midnight on Jan 1, 2024) to avoid DST ambiguity issues at specific moments.
    ref_time = tz1.localize(pytime=pytime(2024, 1, 15, 12, 0, 0))

    # Calculate the offset of each timezone relative to UTC in seconds
    utc_offset_1 = pytz.utc.utcoffset(ref_time) if hasattr(pytz.utc, 'utcoffset') else None
    
    # Get offsets for both zones at our reference time
    from datetime import timedelta
    ref_dt_utc = tz1.localize(pytime(2024, 1, 15, 12, 0, 0)) if hasattr(pytz.utc, 'utcoffset') else None
    
    # Simpler approach: Get the offset of each zone relative to UTC
    try:
        utc = pytz.UTC
        
        dt_utc = datetime(2024, 6, 15, 12, 0, 0) # Fixed date in summer for both zones usually has consistent DST rules or we can pick a non-DST day like Jan 1st to be safe.
        
        # Let's use January 15th to avoid any potential DST confusion at the very start of year if not handled correctly by pytz version, though pytz handles it well.
        dt_utc = datetime(2024, 1, 15, 12, 0, 0) 
        
        offset_1 = tz1.localize(dt_utc).utcoffset()
        offset_2 = tz2.localize(dt_utc).utcoffset()
        
    except Exception as e:
        raise RuntimeError(f"Error calculating timezones: {e}")

    diff_seconds = (offset_2 - offset_1).total_seconds()
    
    # Convert seconds to hours and round to nearest integer if needed, or float. 
    # The task asks for "difference in hours". Usually implies a float or int.
    return round(diff_seconds / 3600)

def main():
    """Main execution block with hard-coded sample values."""
    
    config_content = """timezone: America/New_York
zone: Europe/London"""

    try:
        zones = parse_timezone_config(config_content)
        
        # Calculate the difference based on the parsed zone names
        diff_hours = calculate_hour_difference(zones[0], zones[1])
        
        print(f"Time zone 1 ({zones[0]}): {diff_hours} hours")
    except Exception as e:
        print(f"Error processing configuration or time calculation: {e}")

if __name__ == '__main__':
    main()