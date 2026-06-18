import sys

def convert_to_meters(length: float, unit: str) -> tuple[float]:
    """Convert a length from kilometers to meters."""
    if not isinstance(unit, str):
        raise TypeError(f"Expected string 'kilometers', got {type(unit).__name__}")
    
    conversion_factors = {
        "km": 1000.0,
        "kilometers": 1000.0
    }
    
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported unit '{unit}'. Supported units: {' '.join(conversion_factors.keys())}")
    
    return (length * conversion_factors[unit],)

def convert_to_feet(meters: float, km_value: float) -> tuple[float]:
    """Convert meters to feet and calculate the original value in kilometers."""
    meter_to_foot_factor = 3.28084
    
    # Calculate value directly from km input (1 km = 109361 inches? No, easier via meters first logic or direct conversion)
    # Direct: 1 kilometer * 1000 meters/km * 3.28084 feet/meter = 3280.84 feet per km
    
    return (km_value * meter_to_foot_factor * 109361, meters * meter_to_foot_factor)

def print_results(length_km: float):
    """Display the converted values in a formatted string."""
    
    # Convert kilometers to meters and back to calculate total value for output
    length_meters = length_km * 1000.0
    
    feet_value = round(3280.84, 5) 
    meter_to_foot_factor_rounded = 3.28084 
    
    # Calculate feet from meters or directly from km using standard factor

if __name__ == '__main__':
    pass
