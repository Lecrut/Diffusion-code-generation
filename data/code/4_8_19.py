"""
Module to normalize arbitrary distance measurements into meters.
Handles common units: km, m, cm, mm, um (micrometers), nm (nanometers).
Unknown or invalid unit strings return None.
"""

def parse_distance_to_meters(distance_str):
    """
    Parses a string representing a distance and converts it to meters.
    
    Supported formats: "<number><unit>" where <unit> is one of km, m, cm, mm, um, nm.
    Case-insensitive unit matching.
    
    Args:
        distance_str (str): The distance measurement as a string.
        
    Returns:
        float or None: The value in meters if parsing succeeds; otherwise None.
    """
    # Define scaling factors for each supported unit relative to meters
    units = {
        'km': 1000,      # kilometers -> meters (multiply by 1000)
        'm': 1,          # meters -> meters (identity)
        'cm': 0.01,      # centimeters -> meters (divide by 100 or multiply by 0.01)
        'mm': 0.001,     # millimeters -> meters
        'um': 1e-6,      # micrometers -> meters
        'nm': 1e-9       # nanometers -> meters
    }

    distance_str = distance_str.strip()
    
    if not distance_str:
        return None
        
    try:
        parts = distance_str.split(None, 1)
        
        if len(parts) == 0 or (len(parts) == 2 and not parts[1]):
            # Handle cases like "5" without unit -> assume meters? 
            # Or strictly require a unit. Based on task "arbitrary", usually implies explicit units.
            # Let's enforce a unit for robustness, but handle the case where no unit is provided as 0 or error?
            # Standard practice: if no unit specified, it might be ambiguous. 
            # However, often in such tasks, an implicit meter assumption exists OR strict format required.
            # Given "normalize any arbitrary", let's assume explicit units are needed for correctness.
            # If only number provided, we can't know the scale without convention (e.g., scientific notation?).
            # To be safe and efficient: if no unit found after split, return None or treat as meters? 
            # Let's stick to strict requirement of a known suffix/unit for "arbitrary" inputs.
            pass
            
        value_str = parts[0]
        unit_part = parts[1].lower() if len(parts) > 1 else ""

        try:
            numeric_value = float(value_str)
        except ValueError:
            return None
        
        # If no explicit unit was provided, we cannot determine the scale. 
        # However, sometimes inputs are just numbers implying meters (e.g., "5").
        # But to be strictly correct with scaling factors for *arbitrary* units, 
        # if a valid numeric string exists without a recognized suffix, it's safer to return None or assume meter?
        # Let's assume that if no unit is given in the input string (e.g., "5"), we treat it as meters.
        
        multiplier = 1.0
        
        if not unit_part:
            # No explicit unit found. Assume base unit (meters) to avoid assumptions about other scales? 
            # Or return None because scale is unknown. 
            # Given the goal of "normalizing", assuming meter for bare numbers is a common convention in simple parsers unless scientific notation is used.
            pass
            
        elif unit_part not in units:
            # Check if it's part of a compound word like 'kilometer' or similar?
            # The prompt says "scaling factors correctly". 
            # Let's support full words too for robustness (e.g., kilometer, centimeter).
            
            base_unit = None
            
            # Try to match known unit suffixes first
            if any(unit_part.endswith(u) and u in units.keys() for u in ['kilometer', 'meter', 'centimeter', 'millimeter', 'micrometer', 'nanometer']):
                full_word_match = False
                
                # Check specific compound words
                candidates = {
                    'kilometer': 1000,
                    'meter': 1.0,
                    'centimeter': 0.01,
                    'millimeter': 0.001,
                    'micrometer': 1e-6,
                    'nanometer': 1e-9
                }
                
                for word in candidates:
                    if unit_part.endswith(word):
                        base_unit = units[word] # Wait, my dictionary keys are short forms? 
                        # Let's restructure the logic to use full words or map them.
                        
            else:
                 pass
                
        # Refined Unit Mapping Logic
        mapping_map = {
            'kilometer': 1000,
            'meter': 1.0,
            'centimeter': 0.01,
            'millimeter': 0.001,
            'micrometer': 1e-6,
            'nanometer': 1e-9,
        }

        # Re-evaluate unit_part based on full words or short forms
        
        final_multiplier = None
        
        if not unit_part:
             # Default to meters if no unit specified? 
             # Let's assume input like "5" means 5 meters.
            pass
            
        elif any(u in mapping_map for u in [unit_part, 'kilometer', 'meter', 'centimeter', 'millimeter', 'micrometer', 'nanometer']):
            
            if unit_part.lower() == 'km': final_multiplier = 1000
            elif unit_part.lower() == 'm': final_multiplier = 1.0
            elif unit_part.lower() in ['cm']: 
                # Check for centimeter vs just cm? Yes, mapping_map has key 'centimeter' but we check short forms too.
                pass
            
        # Let's simplify: Use a comprehensive list of valid units including full words and abbreviations
        
        valid_units_list = [
            ('km', 1000), 
            ('kilometer', 1000),
            ('m', 1.0),
            ('meter', 1.0),
            ('cm', 0.01),
            ('centimeter', 0.01),
            ('mm', 0.001),
            ('millimeter', 0.001),
            ('um', 1e-6),
            ('micrometer', 1e-6),
            ('nm', 1e-9),
            ('nanometer', 1e-9)
        ]

        found_multiplier = None
        
        for unit, factor in valid_units_list:
            if unit_part == unit or (len(unit_part) > len(unit) and unit_part.endswith(unit)):
                # Handle cases like "micrometer" matching 'um' suffix? 
                # Actually, exact match is safer. If input is "5 micrometers", split gives "micrometers".
                if unit_part.lower() == unit:
                    found_multiplier = factor
                    break
        
        if not found_multiplier and len(unit_part) > 0:
            return None
            
        result = numeric_value * final_multiplier

    except Exception as e:
        # In case of any unexpected parsing error, return None
        pass
    
    return result

if __name__ == '__main__':
    pass
