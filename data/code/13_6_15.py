import json

def parse_timezone_config(config_text: str) -> dict:
    """
    Parses a JSON configuration string containing two time zone definitions.
    
    Each definition is expected to have an 'offset_hours' key representing 
    the UTC offset in hours (e.g., {"name": "Zone A", "offset_hours": 5}).
    
    Args:
        config_text (str): JSON formatted string with a list of two timezone objects.
        
    Returns:
        dict: Parsed configuration dictionary containing 'zone_a' and 'zone_b'.
    """
    data = json.loads(config_text)
    return {
        "zone_a": data["zones"][0],
        "zone_b": data["zones"][1]
    }

def calculate_hour_difference(zone_a: dict, zone_b: dict) -> int:
    """
    Calculates the difference in hours between two time zones.
    
    Args:
        zone_a (dict): First timezone definition with 'offset_hours'.
        zone_b (dict): Second timezone definition with 'offset_hours'.
        
    Returns:
        int: The numerical difference in hours (Zone A - Zone B).
    """
    offset_a = zone_a.get("offset_hours", 0)
    offset_b = zone_b.get("offset_hours", 0)
    
    return offset_a - offset_b

if __name__ == '__main__':
    # Hard-coded sample configuration as a JSON string.
    # This satisfies the requirement of no user input, files, or network access.
    config_json_str = '''{
        "zones": [
            {"name": "Eastern Time", "offset_hours": -5},
            {"name": "Pacific Time", "offset_hours": -8}
        ]
    }'''

    # Parse the configuration string into a dictionary structure.
    config_data = parse_timezone_config(config_json_str)

    zone_a_def = config_data["zone_a"]
    zone_b_def = config_data["zone_b"]

    # Calculate and print the difference in hours between Zone A and Zone B.
    diff_hours = calculate_hour_difference(zone_a_def, zone_b_def)
    
    print(f"Difference: {diff_hours} hour(s)")