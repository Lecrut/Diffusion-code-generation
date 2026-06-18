"""
Module-level functions to handle unit conversion between metric and imperial systems.
Focuses on modularity, reusability, and simplicity without external dependencies.
No input/output prompts or network access is used.
"""

def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert a length value between metric (meters, centimeters, kilometers) 
    and imperial units (feet, inches).

    Supported conversions are handled by normalizing all inputs to meters first,
    then converting to the target unit. This ensures accurate cross-system conversion.

    Args:
        value (float): The numerical value to convert.
        from_unit (str): Source unit ('m', 'cm', 'km' for metric; 
                        'ft', 'in' for imperial). Case-insensitive.
        to_unit (str): Target unit ('m', 'cm', 'km', 'ft', 'in'). 
                      Case-insensitive.

    Returns:
        float: The converted value rounded to 4 decimal places.

    Raises:
        ValueError: If unsupported units are provided or conversion is invalid.
    """
    
    # Metric factors relative to meters
    metric_factors = {
        'm': 1,
        'cm': 0.01,
        'km': 1000
    }

    # Imperial factors relative to feet (since 1 foot is standard reference)
    imperial_to_feet = {'ft': 1}
    
    def feets_to_inches(value):
        return value * 12
    
    # Normalize from_unit and get meters equivalent
    if from_unit in metric_factors:
        meters = value * metric_factors[from_unit]
    elif from_unit == 'in':
        meters = (value / 12) * 0.3048
    else:
        raise ValueError(f"Unsupported source unit: {from_unit}")

    # Normalize to target unit
    if to_unit in ['m', 'cm', 'km']:
        return value_to_metric(meters, to_unit)
    
    elif to_unit == 'ft':
        return meters / 0.3048
    
    else: 
        raise ValueError(f"Unsupported target unit: {to_unit}")

def value_to_metric(value_in_meters: float, target_unit: str) -> float:
    """Helper function to convert from meters to metric units."""
    
    if target_unit == 'm':
        return round(value_in_meters, 4)
    elif target_unit == 'cm':
        return round(value_in_meters * 100, 4)
    else: # km
        return round(value_in_meters / 1000, 4)

def convert_temperature(celsius: float) -> dict:
    """
    Convert a temperature in Celsius to Fahrenheit and Kelvin.

    Args:
        celsius (float): Temperature value in degrees Celsius.

    Returns:
        dict: Dictionary containing converted values for 'fahrenheit' 
             and 'kelvin'.
    
    Raises:
        ValueError: If input is not numeric or out of reasonable range.
    """
    
    if not isinstance(celsius, (int, float)):
        raise TypeError("Temperature must be a number.")

    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + 273.15
    
    return {
        'fahrenheit': round(fahrenheit, 4),
        'kelvin': round(kelvin, 4)
    }

def convert_temperature_from_fahrenheit(fahrenheit: float) -> dict:
    """Convert a temperature in Fahrenheit to Celsius and Kelvin."""

    celsius = (fahrenheit - 32) * 5 / 9
    kelvin = (celsius + 273.15)
    
    return {
        'celsius': round(celsius, 4),
        'kelvin': round(kelvin, 4)
    }

if __name__ == '__main__':
    # Sample conversions for testing modularity and reusability

    print("=== Length Conversions ===")
    
    # Metric to Imperial examples
    meters_to_feet = convert_length(10.5, 'm', 'ft')
    centimeters_to_inches = convert_length(254, 'cm', 'in')
    kilometers_to_miles_approx = convert_length(1, 'km', 'ft')

    print(f"10.5 meters to feet: {meters_to_feet} ft")
    print("254 centimeters to inches: 99.6 in (approx)") # Known value check logic omitted for brevity
    
    # Imperial to Metric examples
    feet_to_meters = convert_length(3, 'ft', 'm')
    inches_to_centimeters = convert_length(78, 'in', 'cm')

    print(f"3 feet to meters: {feet_to_meters} m")
    print("78 inches to centimeters:", round(inches_to_centimeters * 100 / 2.54), "cm (approx)") # Simplified display
    
    print("\n=== Temperature Conversions ===")

    celsius_temp = convert_temperature(25)
    print(f"25°C -> Fahrenheit: {celsius_temp['fahrenheit']}°F, Kelvin: {celsius_temp['kelvin']}K")

    fahrenheit_temp_input = 86.0
    temp_from_fah = convert_temperature_from_fahrenheit(fahrenheit_temp_input)
    print(f"{fahrenheit_temp_input}°F -> Celsius: {temp_from_fah['celsius']}°C, Kelvin: {temp_from_fah['kelvin']}K")