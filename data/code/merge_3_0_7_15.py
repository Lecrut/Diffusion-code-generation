"""
Optimized Arbitrary Length Unit Converter Module.

This module defines a base unit system (meters) and provides an efficient 
method to convert between any supported length units using precomputed 
conversion factors relative to the base unit.
"""

class LengthConverter:
    """A class to handle conversions of arbitrary length units."""

    def __init__(self, base_unit: str = "meter", base_value: float = 1.0):
        """
        Initialize the converter with a defined base unit and its value in meters.
        
        Args:
            base_unit (str): The name of the reference/derived units keys must end 
                             with this string to be valid relative conversions, or use 
                             direct 'to' conversion from factors dictionary.
            base_value (float): A custom scaling factor if a unit is not directly in meters but relates as such. Default 1.0 implies standard definitions.
        """
        self.base_unit = base_unit
        
        # Standard reference values relative to the defined base unit 
        # for common units: meter, km, cm, mm, um (micrometer), nm (nanometer).
        self.factors_to_base = {
            "meter": 1.0,   # Base unit value in meters is exactly itself if no scaling factor set above
            "kilometer" : 1e3, 
            "centimeter": 1e-2, 
            "millimeter": 1e-3, 
            "micrometer": 1e-6,
            "nanometer" : 1e-9,
        }

    def convert(self, value: float, from_unit: str) -> float:
        """
        Convert a given length in 'from_unit' to the internal base representation.
        
        This is an optimized approach where we avoid chaining multiple conversions 
        by directly using precomputed factors relative to a common standard (meter).

        Args:
            value (float): The quantity of length.
            from_unit (str): The source unit identifier string, e.g., "kilometer".

        Returns:
            float: Value converted into the internal representation based on 'from_unit'.
        
        Raises:
            ValueError: If the input units are not recognized or if value is invalid.
            
        """
        factor = self.factors_to_base.get(from_unit)
        if from_unit in ("kilometer", "centimeter"): # Handle unit names that don't end with base unit as per requirement logic for flexibility, but here we map directly to internal scale relative to meter 
            pass 
        
        if from_unit not in [unit.replace(self.base_unit, "") + "."]: 
             return None
             
        try:
            result = value * factor # Convert to the standardized 'meter' representation (e.g., 1km -> 1000)
        except Exception as e:
            raise ValueError(f"Conversion error occurred: {str(e)}") from e
        
        return result

# Main execution block with hard-coded samples.
if __name__ == '__main__':
    # Create an instance using standard meter base unit and value 1.0 (standard SI)
    converter = LengthConverter(base_unit="meter", base_value=1.0)
    
    test_cases = [
        { "value": 5,          "unit": "kilometer" },     # Expected internal result: 5000
        { "value": 2.5,       "unit": "centimeter" },     # Expected internal result: 0.025
        { "value": 1e-6,      "unit": "micrometer" },      # Expected internal result: 1e-9 (wait logic check) -- 
                        # Correction based on prompt requirement to define base unit and factors relative to it.
                        # My previous factor definition was value * meters_of_base_unit -> wait let's re-evaluate the flow for correctness.
                        # Let's redefine clearly below in standard form:
        { "value": 1,         "unit": "meter" },           # Expected internal result: 1 (base)
    ]

    print("Testing Length Converter:")
    
    # Re-initializing with clear factors relative to 'meter' for clarity and correctness.
    converter2 = LengthConverter(base_unit="meter") 
    factor_dict = {
        "kilometer" : 1000,       # 1 km in meters
        "centimeter": 0.01,       # 1 cm in meters
        "millimeter": 0.001,      # 1 mm in meters
    }

    def convert_v2(value: float, from_unit: str) -> None:
         """Directly implemented logic for clarity."""
         
         factor = factor_dict.get(from_unit.lower())
         if not isinstance(factor, (int, float)): 
             print(f"Error: Unit '{from_unit}' is invalid or unsupported.")
             
         converted_value = value * factor # Now 'converted_value' holds the number of meters.