import configparser

def parse_timezone_offset(timezone_str: str) -> int:
    """
    Parses a timezone string like 'UTC+5' or 'EST-4' to return an integer offset in hours.
    
    Assumptions based on the task constraints (no external libraries, no network):
    - The input format is expected to be a letter(s) followed by +/- and digits representing hours.
    - Minutes are ignored as per "focusing purely on the time scale relationship" for hour differences.
    - If only letters are provided without an explicit offset sign/digits (e.g., 'UTC'), it defaults to 0.

    Args:
        timezone_str (str): The timezone definition string.

    Returns:
        int: The difference in hours relative to UTC or a reference point. 
             Positive for east, negative for west.
    """
    # Remove any whitespace and convert to uppercase for consistency handling if needed, though strict format is assumed.
    s = timezone_str.strip().upper()

    # Check if it's just letters (like 'UTC', 'EST') without an explicit offset suffix in this simplified logic.
    # In a real-world scenario with `pytz` or similar libraries would be used, but the constraint says no external libs/network.
    # We will assume the format is [LETTERS][+-DIGITS]. If digits are missing after sign, treat as 0 for that specific part if we had to guess, 
    # BUT strictly following "reads two time zone definitions", usually implies explicit offsets or standard names mapped locally.
    
    # Since no mapping library exists without network/imports (and imports might be restricted by environment assumptions), 
    # and the task asks to read from a config file which we simulate with hard-coded values in main,
    # let's assume the configuration format provides strings like "UTC+5" or "-4".
    
    if '+' in s:
        sign = 1
        suffix_start_idx = s.index('+') + 1
    elif '-' in s:
        sign = -1
        suffix_start_idx = s.index('-') + 1
    else:
        # No explicit offset found, assume UTC (0) or default to current context which is tricky without libs.
        # Given the constraint of "no pre-existing files" and hardcoding in main, 
        # let's treat pure letters as having an implicit offset we need to derive or just 0 if no digits follow sign.
        # To make it runnable deterministically: assume standard IANA offsets are not available without libs.
        # We will implement a simple parser that expects the +/-HH format explicitly in the config string 
        # provided by our hard-coded sample values below (e.g., "UTC+5", "EST-4").
        return 0

    offset_part = s[suffix_start_idx:]
    
    try:
        hours_str, minutes_str = offset_part.split(':')
        hours = int(hours_str)
        
        # Handle the case where there might be a minute part (e.g. "5:30") -> ignore as per task focus on hour scale relationship? 
        # Or does it imply we should extract just hours from HHMM or H:M format?
        # Let's assume standard ISO-like offset notation often seen in configs: +HH:MM or -HMM.
        
        if ':' in minutes_str and len(minutes_str) > 0:
            try:
                mins = int(minutes_str[:2])
                hours += (mins // 60) # Convert remaining to hours? No, just truncate/floor for "hours difference" focus usually implies integer floor or truncation. 
                                      # Actually, the task says "difference in hours". Usually means total offset / 1 hour rounded/truncated.
            except ValueError:
                mins = int(minutes_str[:2]) if len(minutes_str) >= 2 else 0
        
        return sign * (hours + mins // 60)

    except Exception:
        # Fallback for malformed input in sample data context to ensure robustness without crashing on bad format 
        # but strictly adhering to logic. If no digits found, assume 0 offset relative to base?
        return 0

def calculate_difference(timezone_a_str: str, timezone_b_str: str) -> int:
    """
    Calculates the difference in hours between two time zone definitions.
    
    Args:
        timezone_a_str (str): First timezone string from config.
        timezone_b_str (str): Second timezone string from config.

    Returns:
        int: Difference in hours (offset_A - offset_B).
    """
    return parse_timezone_offset(timezone_a_str) - parse_timezone_offset(timezone_b_str)

if __name__ == '__main__':
    # Hard-coded sample values simulating a configuration file content.
    # Format expected by the parser: "TIMEZONE+OFFSET" or similar without external dependencies.
    config_data = {
        'timezone_a': 'UTC+5',      # Example: 0 + 5 = 5 hours relative to UTC base logic used here? 
                                   # Wait, my parse function treats '+' as sign and digits after it as offset from a zero baseline (like GMT).
                                   # So UTC is usually defined as the reference. If input is 'UTC+5', it means this zone is +5 from UTC.
                                   # But if I treat 'UTC' itself as 0, then 'UTC+5' becomes 5? 
                                   # Let's refine: The task says "reads two time zone definitions".
                                   # Standard interpretation without libs: 
                                   # Zone A = Base (e.g., GMT) + Offset.
                                   # If input is just letters like 'EST', we can't know offset without a map.
                                   # To satisfy the constraint of no external deps/network, and runnable sample:
                                   # We will assume the config file contains explicit offsets relative to UTC in the string itself 
                                   # or simple formats where letters imply known values ONLY IF hardcoded logic is added for common zones?
                                   # No, simpler approach per "no pre-existing files" and "hard-coded":
                                   # Let's define 'UTC' as 0. If a zone has '+5', it is +5 relative to UTC.
                                   # What if the input is just 'EST'? The parser returns 0 (fallback). 
                                   # To make the sample meaningful, let's use explicit offsets in the string like "GMT+3" and "UTC-2".
    }

    tz_a = config_data['timezone_a']   # e.g., GMT+5:30 -> parsed as +5 hours? Or should we handle minutes? 
                                       # My parser does floor division for minutes. 5h30m -> 5.5 * sign.
                                       # Let's check the prompt again: "difference in hours". Usually implies integer or float representing total offset magnitude difference divided by hour unit.
                                       # Since I return int, let's stick to integer truncation of half-hours if needed? 
                                       # Actually `int(5.5)` is 5. If we want precise decimal, use round or keep as float logic then cast.
                                       # Let's assume the sample inputs have clean hour offsets for simplicity unless specified otherwise.

    tz_b = config_data['timezone_b']   # e.g., IST (UTC+5:30) -> +5 hours? 

    # Refined Sample Values to ensure clarity and non-zero difference calculation logic works as expected
    # Let's use explicit formats that clearly denote the offset from a common reference (e.g. UTC).
    
    sample_tz1 = "GMT+2"   # Offset: +2
    sample_tz2 = "UTC-3"   # Offset: -3

    diff_hours = calculate_difference(sample_tz1, sample_tz2)
    
    print(f"Difference between {sample_tz1} and {sample_tz2}: {diff_hours} hours")