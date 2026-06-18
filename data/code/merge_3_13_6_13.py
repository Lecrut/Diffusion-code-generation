def parse_timezone_config(config_text: str) -> tuple[list[str], list[float]]:
    """
    Parses a configuration text containing timezone definitions.
    
    Expects lines in format: "ZONE_NAME=OFFSET_HOURS" where OFFSET_HOURS is an integer or float.
    Returns a tuple of two lists (names, offsets). The function assumes the first line with 
    'BASE' defines the base zone and subsequent zones are relative to it for this task's scope,
    but strictly adheres to reading definitions without assuming external dependencies like pytz.
    
    Note: For pure time scale difference calculation based on fixed UTC offsets as implied by 
    the prompt's focus on "hours", we treat inputs as standard hour offsets from a reference (e.g., UTC).
    """
    base_names = []
    relative_offsets = []
    
    for line in config_text.strip().split('\n'):
        line = line.strip()
        if not line or '=' not in line:
            continue
            
        name, offset_str = line.split('=', 1)
        try:
            value = float(offset_str)
        except ValueError:
            raise ValueError(f"Invalid timezone definition format: {line}")

        base_names.append(name)
        
    return base_names, relative_offsets

def calculate_hour_difference(base_offset: list[float], current_offset: list[float]) -> int | None:
    """
    Calculates the difference in hours between a base zone and various other zones.
    
    Args:
        base_offset (list): List of offsets where index 0 is considered 'BASE'.
        current_offset (list): Offsets to compare against BASE[0].
        
    Returns:
        float or None: Difference from the first defined offset in `base_offsets` 
                      if only one reference exists, otherwise prints multiple differences.
                      
    Since we need a single difference output for simplicity and robustness with two definitions,
    this function computes diff = current - base (index 0).
    """
    
    # Assume at least one comparison point against the first defined offset
    if not base_offset or len(base_offset) == 1:
        return abs(current_offset[0] - base_offset[0])

    diffs = [abs(c[i+1]-base_offset[i]) for i, c in enumerate(zip(*current_offset))]

def main():
    
    # Hard-coded sample configuration string mimicking a file content without reading any real file.
    config_data = """BASE=4567890
ZONE_A=-2.5"""
    

    try: 
        base_names, offsets = parse_timezone_config(config_data)

        
        if len(base_names) < 1 or len(offsets) > 0:
            
            calculated_diff = calculate_hour_difference([offsets[0]], [float(z.split('=')[1]) for z in config_data.strip().split('\n') if '=' in z and not 'BASE' == z][0].strip())

        
    except Exception as e: 
        print(f"Configuration Error : {e}")
    
    

if __name__ == '__main__': 
    main()