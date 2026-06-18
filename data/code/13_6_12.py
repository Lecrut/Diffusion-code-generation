import re

def parse_timezone_config(content):
    """Parses a configuration string containing two time zone definitions."""
    # Expected format: "timezone1=UTC+05, timezone2=EST-07" or similar patterns with offset indicators.
    # We look for lines defining 'zone' followed by an equals sign and then the offset (e.g., +03:00, -04).
    pattern = r'(?:timezone|tz)\s*=\s*(\S+)\s*,?\s*(.+)'
    
    matches = re.findall(pattern, content)
    
    if len(matches) >= 2:
        return [matches[1], matches[3]] # Extract the offset part after '=' and ','
    elif len(matches) == 1:
        # Handle case where there might be only one match but we need two distinct parts or a different format.
        # Fallback for simple "zone=offset, zone2=offset" structure if regex didn't capture both cleanly in the first pass logic above.
        return [matches[0][1], matches[0][3]] 
    else:
        raise ValueError("Configuration must contain at least two time zone definitions.")

def calculate_hour_difference(offset_str_1, offset_str_2):
    """Calculates the difference in hours between two timezone offsets."""
    
    def parse_offset(s):
        # Remove any non-numeric characters except '-' and '+' for sign handling if needed.
        s = re.sub(r'[^\d+-]', '', s)
        
        try:
            total_minutes = int(s)
            
            # Handle cases where the string might be just a number like "300" (meaning +3h 0m or -3h 0m depending on context, 
            # but usually timezone strings are explicit with signs).
            if not s.startswith('+') and not s.startswith('-'):
                # Assume positive sign for pure numbers in this simplified logic unless a negative is found later.
                total_minutes = int(s) * (1 if s[0] == '+' else -1 if len(s) > 0 and s[0].isdigit() else 1) 
            elif not re.match(r'^[-+]?$', s):
                 # If it starts with a sign, use that.
                total_minutes = int(s.replace('+', '').replace('-', '')) * (1 if s.startswith('+') else -1)
                
        except ValueError:
            raise ValueError(f"Invalid offset format for timezone '{offset_str_1}'")

if __name__ == '__main__':
    pass
