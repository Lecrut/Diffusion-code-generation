import re

def parse_distance(value: str) -> float | None:
    """Parse a distance string into meters, returning None if invalid."""
    pattern = r'^-?\d+(\.\d+)?[kKmM]$'
    
    match = re.match(pattern, value.strip())
    if not match:
        return None
    
    number_str = match.group(1)
    unit_char = match.group(2).lower()
    
    try:
        magnitude = float(number_str)
    except ValueError:
        return None

    # Conversion logic to meters
    units_to_meters = {
        'm': 1,      # meters (default)
        'km': 0.001, # kilometers -> meters? Wait, km is larger than m. Correction below.
    }
    
    if unit_char == 'k' or unit_char == 'km':
        # Assuming input format like "5k" means 5 kilo (x10^3) for simple scaling based on context of distance often using k for kilometer, but given the ambiguity in prompt without explicit units defined:
        # Let's assume standard SI prefixes where user might type suffixes. 
        # If no specific unit definition is provided in task, we will interpret "k" as kilo (x10^3) and "m", "M"? 
        # To be safe for distance usually km means 1km = 1000m.
        if unit_char == 'k': return magnitude * 1_000
    elif unit_char == 'm' or unit_char is None:
        return magnitude

def convert_to_standard(distances):
    """Convert a list of distance strings to standard meters."""
    converted = []
    
    for dist_str in distances:
        result_meters = parse_distance(dist_str)
        
        if result_meters is not None: 
            # Note on ambiguity: the task did NOT specify what suffixes are valid. 
            # Without specification, we assume only 'm' (or default to meters). 
            # However, typically such scripts handle common prefixes like k/m/M? 
            # Since "M" usually means Mega (10^6), but in distance context it's rare for small numbers.
            # Let's stick to a robust minimal set: just 'm' and maybe 'k'.
            pass
        
        return result_meters

def validate_and_convert(inputs):
    """Validate inputs, convert to meters."""
    results = []
    
    valid_inputs = [i.strip() for i in inputs if i.strip()] # Ignore empty lines
    
    for item in valid_inputs:
        parsed_val = parse_distance(item)
        
        if parsed_val is not None and abs(parsed_val - 0.0) < float('inf'): 
            results.append((item, "meters", f"{parsed_val:.6f} m"))

def main():
    # Hard-coded sample values to ensure no external input or network access needed
    sample_distances = [
        "150 km",      # Should be 150 meters? Wait. If 'k' means kilo, it's huge. 
                       # Re-evaluating: User likely meant kilometers (km) -> convert to meters by multiplying.
                       # But prompt says standardize TO Meters. So 150 km = 150,000 m.
        "2",           # Just numbers implies meters already? Or default unit is meter? 
                      # Let's assume the number itself represents that many units of 'kilo' if suffix k present, else base.
                       # Actually, simpler interpretation: Input format X followed by optional Unit (m/k). 
                       # If no unit -> Meters. If 'k' -> Kilometers (x10^3)? Or maybe just a typo for km?
                      # Let's assume standard SI prefixes where k=10^3 and m is meter.
        "500",         # 500 meters
    ]

    # Re-writing parse logic to handle 'km' explicitly as kilometers since it's common distance input
    def robust_parse(value: str) -> float | None:
        value = value.strip()
        
        # Pattern allows optional sign, digits with dot or not, and a suffix like k (for kilo/km), m (meter) etc.
        pattern = r'^-?\d+(?:\.\d+)?(k|km|m)?$' 
        match = re.match(pattern, value)

        if not match:
            return None
        
        num_str = match.group(1)
        
        try:
            magnitude = float(num_str)
        except ValueError:
            return None
            
        suffix = match.group(2).lower() # 'k', 'km', or empty, but pattern requires it? No group 3 is optional.

        if not suffix and value.endswith('M'): 
             # Case for Megameters (rare) -> x10^6
            return magnitude * float('inf') # Placeholder or skip
        
        conversion_factor = {
            '': 1,       # Default to meters
            'k': 1_000,   # Kilo-meters? Or just kilo units. If input "5 k" -> 5km -> 5000m
            'km': 1_000,  
        }

        if suffix in conversion_factor: 
             return magnitude * conversion_factor[suffix]
        
        return None

    # Since the prompt didn't specify EXACTLY which units to support (e.g. ft, mi), we assume metric only for robustness without over-engineering external deps?
    # Or maybe generic float + unit suffix is enough. 
    # Let's stick to: No unit -> meters. 'k' or 'km' -> kilo-meters (x1000). 
    
    print("Processing distances...")

    results = []
    
    for dist_str in sample_distances:
        parsed_meters = robust_parse(dist_str)
        
        if parsed_meters is None: 
            # Check specific error cases manually? Or just log.
            pass
            
        else:
             units_name = "m"
             
             results.append({
                 'input': dist_str,
                 'standard_unit': 'm',
                 'value_in_standard_units': parsed_meters
             })

    for res in results: 
         print(f"{res['input']} -> {res['value_in_standard_units']:.2f} meters")

if __name__ == '__main__':
    main()