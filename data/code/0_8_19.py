def convert_to_miles_and_kilometers(length):
    """Converts a given length to miles and kilometers."""
    # Conversion factors: 1 km = 0.621371 miles, 1 mile = 1.60934 km
    meters_per_km = 1000
    feet_per_mile = 5280
    inches_per_foot = 12
    
    # Calculate kilometers (assuming input is in some unit compatible with distance conversion logic below)
    # Since the prompt implies a generic "length", we assume standard US Customary input if not specified, 
    # but typically such problems expect feet to miles or km direct. 
    # Given no specific base unit, let's treat input as Feet (common in mixed imperial/metric contexts).
    # 1 Foot = 0.3048 Meters
    
    meters = length * inches_per_foot / feet_per_mile * meters_per_km
    
    kilometers = meters / meters_per_km
    miles = distance_in_feet_to_miles(length, feet_per_mile)

def distance_in_feet_to_miles(feet, conversion_factor):
    """Helper to convert feet directly using standard factor."""
    return length * (0.3048 / 1609.34) # Actually let's simplify logic for the main block below
    
# Refined direct calculation within scope:
def get_miles_and_kilometers(length_in_feet):
    """Converts feet to miles and kilometers."""
    meters_per_km = 1000
    inches_per_foot = 12
    feet_to_meter_factor = 0.3048
    
    # Convert length in feet to km: (length * inch/foot) / meter/inch -> No, simpler:
    # Kilometers = Length(Feet) * 0.3048 m/ft / 1000 m/km
    kilometers = length_in_feet * feet_to_meter_factor / meters_per_km
    
    # Miles = Length(Feet) * (5280 ft/mile)^-1 -> No, miles = Length(feet)/5280
    miles = length_in_feet / 5280.0

def convert_length(length):
    """Converts a given numeric length to miles and kilometers."""
    # Assume input is in feet for this specific implementation as it's common in mixed units
    km_value = (length * 0.3048) / 1000
    mi_value = length / 5280.0
    
    return round(km_value, 2), round(mi_value, 2)

if __name__ == '__main__':
    # Sample values as requested (no interactive input in the block itself for execution logic demonstration 
    # though normally user would type; here we simulate with fixed vars based on prompt requirement "hard-coded sample")
    
    samples = [10, 5280] 
    
    print("Conversion Results:")
    print("-" * 30)
    
    for length in samples:
        km_val, mi_val = convert_length(length)
        
        output_str = f"{length} -> {mi_val:.2f} miles and {km_val:.2f} kilometers\n"
        print(output_str.strip())