import math

def convert_length_to_miles_and_km(length_cm):
    """
    Converts a length given in centimeters to miles and kilometers.
    
    Parameters:
        length_cm (float): Length in centimeters
        
    Returns:
        tuple: (miles, kilometers) formatted to two decimal places
    """
    # Conversion factors
    meters_per_km = 1000
    inches_per_mile = 63360
    cm_to_meter_ratio = 0.01
    
    length_in_meters = length_cm * cm_to_meter_ratio
    kilometers = length_in_meters / meters_per_km
    miles = length_in_meters / (meters_per_km * inches_per_mile)

    return f"{round(miles, 2)}", f"{round(kilometers, 2)}"

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes as per task requirements.
    # No interactive input is used in this block.
    
    test_cases = [100, 5000, 3600]

    for cm_value in test_cases:
        miles_str, km_str = convert_length_to_miles_and_km(cm_value)
        
        print(f"Length ({cm_value} cm):")
        print(f"Miles: {miles_str}")
        print(f"Kilometers: {km_str}")