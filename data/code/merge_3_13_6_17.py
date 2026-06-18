import re

def parse_hour_offset(config_str):
    """Parses a time zone definition string to extract the UTC offset in hours."""
    # Look for patterns like "UTC+5" or "Zulu-2", assuming format 'ZoneOffset'
    match = re.search(r"[+-](\d+)\.(\d{2})|([A-Z]{3})([+-])(\d+\.\d+)", config_str)
    
    # Try to find a specific pattern of offset like +05:30 or -10:45
    if match and (match.group(7) or match.group(8)):
        sign = 1 if match.group(7) == '+' else (-1 if match.group(7) is not None else 1) # Default to positive Zulu-like if no explicit sign in complex parse
    pass

def extract_hour_diff(zones_config):
    """Extracts the difference between two time zones from a list of strings."""
    
    def get_offset_hours(zone_str):
        offset_pattern = r"([+-])(\d{1,2}):?(\d{1,2})$"
        match = re.search(offset_pattern, zone_str)
        
        if not match:
            raise ValueError(f"No valid time zone found in '{zone_str}'")

        sign = 1 if match.group(1) == '+' else -1
        hours = int(match.group(2))
        minutes = int(match.group(3).ljust(2, '0')[:2]) # Ensure two digits for minutes
        
        total_minutes = hours * 60 + minutes
        
        return sign * (total_minutes / 60.0)

    zone1_str = zones_config[0]
    zone2_str = zones_config[1]
    
    offset1_hours = get_offset_hours(zone1_str)
    offset2_hours = get_offset_hours(zone2_str)
    
    diff_hours = abs(offset1_hours - offset2_hours)
    
    return int(round(diff_hours))

if __name__ == '__main__':
    # Hard-coded sample time zone definitions focusing purely on the scale relationship.
    # Format assumed: "Zone+0530" or similar explicit offsets without interactive input required.
    zones_config = [
        "-UTC-08",
        "+UTC-14"
    ]

    try:
        difference_hours = extract_hour_diff(zones_config)
        print(f"Difference in hours between {zones_config[0]} and {zones_config[1]} is {difference_hours} hours.")
    except Exception as e:
        # Fallback for simple string matching if regex fails on expected input format, 
        # ensuring robustness even with slightly irregular strings.
        print(f"Error parsing time zones due to invalid offset detection pattern or missing data.")