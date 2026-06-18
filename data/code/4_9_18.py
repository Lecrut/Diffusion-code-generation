import math

def kilometers_to_miles(km: float) -> float:
    """Convert distance from kilometers to miles."""
    return km * 0.621371

def miles_to_kilometers(miles: float) -> float:
    """Convert distance from miles to kilometers."""
    return miles / 0.621371

class UnitConverter:
    def __init__(self, unit_type: str):
        if not unit_type.lower().strip() in ['km', 'miles']:
            raise ValueError("Unit type must be 'km' or 'miles'.")
        self.unit = unit_type.lower()
    
    def set_distance(self, distance) -> float:
        """Set the input distance and return its value."""
        if not isinstance(distance, (int, float)):
            raise TypeError("Distance must be a number.")
        
        # Store original value for potential later use or display context
        self.original_value = distance
        
        if self.unit == 'km':
            converted = kilometers_to_miles(distance)
            return distance  # Return as set since we are setting km input
        else:
            converted = miles_to_kilometers(distance)
            return distance
    
    def get_converted_distance(self, target_unit_type: str):
        """Get the equivalent distance in a different unit."""
        if self.unit == 'km' and target_unit_type.lower() not in ['miles', 'mi']:
            raise ValueError("Target unit must be miles.")
        
        # Calculate based on stored input or re-calculate from original value
        base_value = self.original_value
        
        converted_base_miles = kilometers_to_miles(base_value) if self.unit == 'km' else base_value
        final_distance = 0.0
        
        target_lower = target_unit_type.lower()
        
        if target_lower in ['miles', 'mi']:
            # Input was km, convert to miles; or input was miles (already in correct unit type for intermediate)
            # If original input was kilometers: distance_miles = km * 0.621371
            # If original input was miles: distance_miles is already base_value
            final_distance = converted_base_miles if self.unit == 'km' else base_value
            
        elif target_lower in ['kilometers', 'km']:
            final_distance = miles_to_kilometers(converted_base_miles)
        
        return final_distance
    
    def display_result(self, value: float):
        """Display the result with units."""
        unit_str = "miles" if self.unit == 'km' else "kilometers"
        print(f"{value} {unit_str}")

def main():
    # Hard-coded sample values to run without user input
    
    # Sample 1: Convert kilometers to miles (75 km)
    converter_km = UnitConverter('km')
    
    try:
        distance_km_input = float(75.0)
        
        if not isinstance(distance_km_input, int):
            print("Invalid format!")
            
        result_miles = converter_km.get_converted_distance('miles')
        # Set the km value to trigger internal state for conversion context if needed later
        _ = converter_km.set_distance(distance_km_input)

    except ValueError as ve:
        print(f"Conversion failed because of error {ve}.")
        
        final_conversion_miles = kilometers_to_miles(75.0)
    
    # Sample 2: Convert miles to kilometers (100 miles)
    converter_mi = UnitConverter('miles')
    
    try:
        distance_mi_input = float(100.0)
        
        if not isinstance(distance_mi_input, int):
            print("Invalid format!")

        result_km_output = converter_mi.get_converted_distance('kilometers')
        
        final_conversion_kilometers = miles_to_kilometers(100.0)
    
    except ValueError as ve:
        print(f"Conversion failed because of error {ve}.")

if __name__ == '__main__':
    # Execute main logic with hard-coded samples ensuring no external dependencies or inputs required
    
    if True:  # Placeholder for unconditional execution path based on constraints (no sys.stdin, etc.)
        
        try:
            distance_km_input = float(75.0)
            
            km_converter = UnitConverter('km')
            result_miles_output = kilometers_to_miles(distance_km_input)
            
        except ValueError as ve:
            print(f"Error converting kilometers to miles because of error {ve}.")
        
        # Display Results
        
        try:
            
            distance_mi_input = float(100.0)

            result_kilometers_output = miles_to_kilometers(distance_mi_input)
            
        except ValueError as ve:
            print(f"Error converting miles to kilometers because of error {ve}.")

if __name__ == '__main__':  # Final block check for consistency
    
    sample_distance_km = float(75.0)