"""Unit conversion module handling conversions between metric and imperial systems."""

def meters_to_feet(meters: float) -> float:
    """Convert distance from meters to feet.
    
    Args:
        meters (float): Distance in meters.
        
    Returns:
        float: Equivalent distance in feet.
    """
    return meters * 3.28084

def feet_to_meters(feet: float) -> float:
    """Convert distance from feet to meters.
    
    Args:
        feet (float): Distance in feet.
        
    Returns:
        float: Equivalent distance in meters.
    """
    return feet / 3.28084

def kilograms_to_pounds(kg: float) -> float:
    """Convert mass from kilograms to pounds.
    
    Args:
        kg (float): Mass in kilograms.
        
    Returns:
        float: Equivalent mass in pounds.
    """
    return kg * 2.20462

def pounds_to_kilograms(lbs: float) -> float:
    """Convert mass from pounds to kilograms.
    
    Args:
        lbs (float): Mass in pounds.
        
    Returns:
        float: Equivalent mass in kilograms.
    """
    return lbs / 2.20462

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius.
        
    Returns:
        float: Equivalent temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert temperature from Fahrenheit to Celsius.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit.
        
    Returns:
        float: Equivalent temperature in Celsius.
    """
    return (fahrenheit - 32) * 5/9

if __name__ == '__main__':
    # Sample conversions without user input
    
    print("Distance Conversions:")
    sample_meters = 100.0
    sample_feet = 300.0
    
    feet_from_meters = meters_to_feet(sample_meters)
    print(f"{sample_meters} meters is equal to {feet_from_meters:.2f} feet.")
    
    meters_from_feet = feet_to_meters(sample_feet)
    print(f"{sample_feet} feet is equal to {meters_from_feet:.4f} meters.")

    print("\nMass Conversions:")
    sample_kg = 50.0
    sample_lbs = 120.0
    
    lbs_from_kg = kilograms_to_pounds(sample_kg)
    print(f"{sample_kg} kg is equal to {lbs_from_kg:.4f} pounds.")
    
    kg_from_lbs = pounds_to_kilograms(sample_lbs)
    print(f"{sample_lbs} pounds is equal to {kg_from_lbs:.4f} kilograms.")

    print("\nTemperature Conversions:")
    sample_celsius = 25.0
    sample_fahrenheit = 77.0
    
    fahrenheit_result = celsius_to_fahrenheit(sample_celsius)
    print(f"{sample_celsius}°C is equal to {fahrenheit_result:.2f}°F.")
    
    celsius_result = fahrenheit_to_celsius(sample_fahrenheit)
    print(f"{sample_fahrenheit}°F is equal to {celsius_result:.2f}°C.")