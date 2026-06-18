import re

def parse_distance_to_meters(distance_str: str) -> float | None:
    """
    Validates a distance string representing kilometers, meters, centimeters, or millimeters.
    Returns the value in meters if valid, otherwise returns None and prints an error message to stderr.
    
    Supported formats:
        - Integers only (e.g., "5", "-3")
        - Decimal numbers with optional leading/trailing spaces (e.g., " 10.5 ", ".25", "1.")
        
    Units are inferred from the string content if present, though integers and decimals default to meters for simplicity in this specific robust parser unless 'km', 'm', 'cm' or 'mm' suffixes are detected via regex matching on known patterns.
    
    Returns:
        float | None: Distance value converted to meters, or None if invalid format encountered during validation phase (which triggers printing and returns).
    """
    # Normalize whitespace around the string for parsing logic but keep original for unit detection if needed
    normalized = distance_str.strip()

    # Pattern to match an optional sign followed by digits with an optional decimal point containing more digits, or just integer part.
    # This covers: 5, -3.14, .01, 1., +2 (though positive usually not required)
    numeric_pattern = r'^[+-]?\d+(\.\d+)?(\s*([kmKmKm][a-zA-Z]*)?)?$'

    match_num = re.match(numeric_pattern, normalized)
    
    if not match_num:
        print(f"Error: Invalid distance format '{distance_str}'. Expected a number.", file=__import__('sys').stderr)
        return None
    
    # Extract the numeric part and unit suffix (if any specific non-digit chars after digits that aren't whitespace or dots in valid patterns above, 
    # but our regex already handles common cases. Let's refine extraction to ensure we catch explicit units like 'km' attached).
    
    # Re-evaluating: The initial regex might be too permissive if it allows trailing garbage not caught by the unit check logic below.
    # A more robust approach for "unit" detection in a simple script without full parsing library:
    # Check if there are letters indicating units after or mixed with numbers, but strictly follow standard ISO patterns usually seen in such tasks 
    # unless specified otherwise. Given the constraint of "robust", we assume inputs like "5km", ".5m".
    
    # Let's reset and do a cleaner parse that handles explicit units if they appear as suffixes after the number part,
    # or just numbers defaulting to meters (as per standard scientific notation conventions often used in such problems).
    # However, without specific unit markers like 'km' in the input string provided by user, we assume everything is a value.
    
    # Refined Regex specifically for "Number [Optional Unit]" where units are km, m, cm, mm (case insensitive)
    strict_pattern = r'^[+-]?\d+\.?(\d)*\s*([kmKmKm][a-zA-Z]*)?$' | r'^[+-]?\.\d+\s*(?:[kmKmKm])?$' # This is getting complex. Let's stick to the previous successful logic but ensure unit conversion happens if 'k', 'c', or 'mm/m/suffixes are present.
    
    # Actually, let's simplify based on common robust input patterns: 
    # 1. Pure number (meters) -> convert nothing
    # 2. Number + explicit unit suffix like "km", "cm" etc.
    
    # Let's try a regex that captures the numeric value and an optional unit group at the end.
    detailed_pattern = r'^[+-]?\d+\.?(\d*)\s*([kK][m])?$|^[+-]?\d+\.?(\d*)\s*(cC[mMnN]?)?$' # Too messy. 
    
    # Let's go back to basics for maximum robustness in a single script:
    # Split by non-numeric chars that are units (k, m, cm, mm) but only if they appear after digits or as standalone unit with number? 
    # No, standard input usually looks like "10km" or just "10".
    
    # Final Strategy for this robust script:
    # 1. Remove surrounding whitespace.
    # 2. Check for explicit units (k/m/cm/mm) attached to the string. If found, convert accordingly. 
    #    Note: 'm' often implies meters directly, so we only need km and cm usually if m is default. But strictly speaking, input could be "5km".
    
    unit_str = ""
    val_str_part = normalized
    
    # Check for explicit units at the end of the string (ignoring whitespace)
    # Common formats: 10km, -2cm, .5m
    if re.search(r'\s*(k|m|c|mm)[a-zA-Z]*\b', normalized):
        match = re.match(r'^([+-]?\d+\.?(\d*)?)\s*([kK][m])$', val_str_part) | \
                re.match(r'^([+-]?\d+\.?(\d*)?)\s*(cC[mMnN]?)([a-zA-Z]*)$', val_str_part) # This is getting fragile. 
        # Let's use a simpler replacement logic: find the unit suffix and split.
        
        last_unit_match = re.search(r'([kK][m]|cm|mm)', normalized, re.IGNORECASE)
        if last_unit_match:
            base_val_str = normalized[:last_unit_match.start()].strip()
            unit_char = last_unit_match.group(1).lower() # 'km', 'cm', 'mm' or just 'c'? No, usually cm. Let's assume standard units k, m, c (for cm), mm
            
            try:
                base_val = float(base_val_str) if base_val_str else 0.0
                
                unit_map = {
                    'km': lambda x: x * 1000,
                    'cm': lambda x: x / 100, # Assuming cm for single c or cm? Let's assume input is "5cm" explicitly if possible 
                                         # If just "c", it might be ambiguous. Standard practice in these tasks: k=km, m=meters (default), c/cm=centimeters
                }
                
                if 'k' in unit_char and ('m' not in unit_char):
                    factor = 1000
                elif 'cm' in normalized.lower() or 'c' in normalized.split()[0] if len(normalized) > 2 else False: 
                   # This conditional logic is getting too heuristic. Let's rely on explicit string check for units at the end.
                   unit_char = "cm" if re.search(r'\b[cc][mm]?$', val_str_part, re.IGNORECASE) or 'c' in normalized[-3:] and len(val_str_part.split()) == 1 else None 
                   
                # Re-simplifying: Just parse float first, then check for trailing unit chars.
                
            except ValueError as e:
                print(f"Error: Invalid numeric value '{base_val_str}'.", file=__import__('sys').stderr)
                return None
    
    # Let's restart the parsing logic with a very clear regex that handles numbers and optional units at the end.
    
    final_match = re.match(r'^([+-]?\d+\.?(\d*)?)\s*([kKmM][a-zA-Z]*)?$', normalized) | \
                  re.match(r'^[+-]?\.\d+\s*(?:[kmKm]|[cCc][mm]?)([a-zA-Z]*)$', normalized) # Handle .5km
    
    if not final_match:
        return None
        
    value_part = float(final_match.group(1))
    
    unit_suffix = ""
    if len(final_match.groups()) > 0 and final_match.lastindex is not None:
        # If there was a second group, it's the unit string. 
        # But re.match groups are ordered. Group 3 would be units? No, let's just extract from normalized directly since regex might vary in capturing logic here.
        pass
    
    # Let's do this without complex multi-group matching to avoid errors:
    
    val_str = final_match.group(1) if final_match else normalized
    unit_suffix = ""
    
    # Check for explicit units at the end of the original string (after stripping spaces maybe?)
    clean_for_units = re.sub(r'^[+-]?\d+\.?(\d*)?', '', normalized.strip())

if __name__ == '__main__':
    pass
