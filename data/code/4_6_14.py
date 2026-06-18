"""
Distance Unit Converter Module

This module provides functionality to convert distances between various units of measurement.
It supports conversion from any supported source unit to a specified target unit, with clear error handling.

Supported Units:
- kilometers (km)
- miles (mi)
- meters (m)
- feet (ft)
- yards (yd)
- centimeters (cm)
- inches (in)

Conversion Logic:
All units are normalized to meters for internal calculation, then converted to the target unit.
This ensures accuracy across all supported pairs.

Error Handling:
- Invalid input types raise a TypeError.
- Unknown source or target units raise a ValueError with specific messages.
- Zero distance is handled gracefully (returns 0).
"""

class DistanceConverter:
    """A class to handle distance unit conversions."""
    
    # Conversion factors relative to meters
    METERS = {
        'km': 1_000,      # kilometers per meter? No, km * 1000 = m. So factor is 1/1000 of a meter in terms of value? 
                         # Let's define: unit_value_in_meters = input_distance * conversion_factor
        'm': 1,           # meters
        'cm': 0.01,       # centimeters (divide by 100) -> wait, cm is smaller. 
                         # If I have 100 cm, that's 1 m. So factor should be such that distance * factor = meters.
                         # Therefore: km=1000, mi=?, m=1, ft=0.3048...
        'ft': 0.3048,     # feet (multiply by this to get meters) -> No! 
                         # Standard definition: 1 foot = 0.3048 meters exactly.
                         # So if input is in feet, value_in_meters = distance * 0.3048? NO.
                         # If I have 2 ft, that's 0.6096 m. Yes. 
                         # Wait, let's re-verify standard factors relative to meters:
                         # km -> multiply by 1000 gives meters. So factor = 1000? No.
                         # Let d be distance in unit U. Meters = d * (meters_per_unit).
                         # For km: 1 km = 1000 m. Factor = 1000. Correct.
                         # For cm: 1 cm = 0.01 m. Factor = 0.01. Correct.
        'yd': 0.9144,     # yards (1 yard = 0.9144 meters) -> Wait, standard is ~3 feet? 
                         # Yes, 1 yd = 3 ft = 3 * 0.3048 m = 0.9144 m. Correct.
        'mi': 1609.344,   # miles (1 mile = 1609.344 meters) -> Wait, usually we multiply distance by factor to get base? 
                         # Yes: d_miles * 1609.344 = meters. Correct.
        'in': 0.0254      # inches (1 inch = 0.0254 meters) -> Wait, usually we multiply distance by factor to get base? 
                         # Yes: d_inches * 0.0254 = meters. Correct.
    }

    def __init__(self):
        """Initialize the converter with supported units."""
        self.supported_units = set(self.METERS.keys())
    
    def convert_distance(self, distance, source_unit, target_unit) -> float:
        """
        Convert a distance from one unit to another.
        
        Args:
            distance (float or int): The numerical value of the distance.
            source_unit (str): The original unit of measurement.
            target_unit (str): The desired unit for conversion.
            
        Returns:
            float: The converted distance in the target unit.
            
        Raises:
            TypeError: If input types are not numeric or strings.
            ValueError: If units are unknown, empty string, or source equals target with invalid logic? 
                       (Actually if same unit it should work fine).
        """
        # Type validation for distance
        try:
            num_distance = float(distance)
        except TypeError:
            raise TypeError(f"Distance must be a number. Received type {type(distance).__name__}")

        # Validate source and target units against supported list
        if not isinstance(source_unit, str):
            raise TypeError("Source unit must be a string.")
        if not isinstance(target_unit, str):
            raise TypeError("Target unit must be a string.")
        
        if len(source_unit) == 0 or len(target_unit) == 0:
            raise ValueError("Unit strings cannot be empty.")

        source_lower = source_unit.lower().strip()
        target_lower = target_unit.lower().strip()

        # Check for valid units in the supported set
        if source_lower not in self.supported_units:
            available_list = ", ".join(sorted(self.supported_units))
            raise ValueError(f"Unsupported unit '{source_unit}'. Supported units are: {available_list}")
        
        if target_lower not in self.supported_units:
            available_list = ", ".join(sorted(self.supported_units))
            raise ValueError(f"Unsupported unit '{target_unit}'. Supported units are: {available_list}")

        # Handle zero distance gracefully to avoid potential division by zero issues later, 
        # though the math handles it naturally. Still good for clarity.
        if num_distance == 0:
            return 0.0
        
        # Convert source unit to meters first
        value_in_meters = num_distance * self.METERS[source_lower]
        
        # Then convert from meters to target unit
        factor_to_target = self.METERS[target_lower]
        
        if abs(factor_to_target) < 1e-9: 
            raise ValueError(f"Cannot convert to zero-sized unit '{target_unit}'.")

        result_in_target = value_in_meters / factor_to_target
        
        return round(result_in_target, 6)

def main():
    """
    Main execution block with hard-coded sample values.
    Demonstrates usage without any user input or external dependencies.
    """
    
    # Instantiate the converter
    converter = DistanceConverter()

    print("Distance Unit Converter")
    print("-" * 30)

    # Sample Test Cases
    test_cases = [
        {"distance": 1, "source": "km", "target": "mi"},       # 1 km to miles
        {"distance": 5280, "source": "ft", "target": "m"},     # 5280 ft (1 mile) to meters
        {"distance": 1609.344, "source": "m", "target": "km"}, # 1 km in reverse check
        {"distance": 100, "source": "cm", "target": "in"},     # 100 cm to inches (approx)
        {"distance": -5, "source": "mi", "target": "ft"},      # Negative distance handling
    ]

    for i, case in enumerate(test_cases):
        d = case["distance"]
        src = case["source"]
        tgt = case["target"]
        
        try:
            result = converter.convert_distance(d, src, tgt)
            
            print(f"\nTest Case {i + 1}:")
            print(f"Input:   {d} {src}")
            print(f"Output:  {result:.6f} {tgt}")

        except Exception as e:
            # In a real app we might log, but here just print the error for visibility 
            # since no external logging is requested.
            print(f"\nTest Case {i + 1}: Error - {e}")

if __name__ == '__main__':
    main()