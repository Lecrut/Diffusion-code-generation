"""
Unit Conversion Module: Handles conversions between Metric (SI) and Imperial systems.
Designed for modularity, reusability, and ease of testing without external dependencies or I/O.
"""

class UnitConverter:
    """A class to handle unit conversion operations."""

    def __init__(self):
        # Base units definitions relative to standard SI/Imperial standards
        self._lengths = {
            'meter': 1,       # Reference for meters
            'kilometer': 0.001,
            'centimeter': 100,
            'millimeter': 1000,
            'inch': 254/3937, # inches to cm approx (actually defined as exact conversion factor later)
        }

    def convert_length(self, value: float, from_unit: str, to_unit: str) -> float:
        """Convert a length value between different units.
        
        Args:
            value: The numerical value to convert.
            from_unit: Source unit string (e.g., 'm', 'km').
            to_unit: Target unit string (e.g., 'ft', 'in').

        Returns:
            Converted float value or 0 if units are invalid.
        
        Raises:
            ValueError: If input is not a number or unsupported unit provided.
        """
        valid_units = ['meter', 'kilometer', 'centimeter', 'millimeter', 
                      'inch', 'foot']

        # Normalize input values to lowercase for consistent handling
        from_unit_lower = from_unit.lower() if isinstance(from_unit, str) else None
        to_unit_lower = to_unit.lower() if isinstance(to_unit, str) else None
        
        if not (from_unit_lower and to_unit_lower):
            raise ValueError("Invalid unit specification. Use 'm', 'km', 'cm', 'mm' for metric or 'in', 'ft' for imperial.")

        # Map user-friendly names to internal keys
        from_key = {
            "meter": "meter", "kilometer": "kilometer", 
            "centimeter": "centimeter", "millimeter": "millimeter"
        }.get(from_unit_lower, None) or \
                  {"meters": "meter", "km": "kilometer"}[from_unit_lower]

        to_key = {
            "inch": "inch", "foot": "foot" # Note: 'ft' is not in this specific mapping block but we'll handle it below
            
        }.get(to_unit_lower, None) or \
                 {"inches": "inch"}[to_unit_lower]

        if from_key == to_key and value != 0:
            return float(value) # No conversion needed
        
        try:
            base_value = self._convert_to_base(from_key, value)
            
            final_result = self._convert_from_base(to_key, base_value)
            return round(final_result, 4)

        except Exception as e:
            print(f"Conversion error for {from_unit} to {to_unit}: {e}")
            raise ValueError("Error during conversion process.") from None
    
    def _convert_to_base(self, unit_name: str, value: float) -> float:
        """Convert any input unit to the base metric system (meters)."""
        
        if not isinstance(value, (int, float)):
            raise TypeError(f"Value must be a number. Got {type(value)}")

        # Metric Base Conversion Factors relative to meters
        factors = {
            'meter': 1.0,
            'kilometer': 1e3,
            'centimeter': 1e-2,
            'millimeter': 1e-3,
            'inch': 0.0254, # Exact: 1 inch = 0.0254 meters
            
        }

        return value * factors[unit_name] if unit_name in factors else self._convert_to_base('meter', value)

    def _convert_from_base(self, target_unit: str, base_value: float) -> float:
        """Convert the metric base (meters) to a specific target unit."""
        
        # Imperial Base Conversion Factors relative to meters
        
        conversion_factors = {
            'inch': 1/0.0254, 
            'foot': 393700.787 / 3937, # Approximate exact: 1 foot = 0.3048 m -> factor is ~3.28 ft/m
        }

        if target_unit == "inch":
            return base_value * (1/0.0254)
        
        elif target_unit == 'foot':
            return base_value / 0.3048
        
        else: 
             # Fallback for other units not explicitly handled in this simplified logic, though we define them above
            raise ValueError(f"Unsupported unit conversion to {target_unit}. Supported: inch, foot.")

    def convert_temperature(self, value: float, from_temp: str, to_temp: str) -> float:
        """Convert temperature between Celsius and Fahrenheit.
        
        Args:
            value: Temperature in degrees C or F.
            from_temp: Source unit ('c' for Celsius, 'f' for Fahrenheit).
            to_temp: Target unit ('c', 'f').

        Returns:
            Converted float temperature rounded to 2 decimal places.
        """
        
        valid_from = ['celsius', 'centigrade'] # Using aliases like c -> celsius
        valid_to = ['fahrenheit', 'far'] 

        from_name_lower = from_temp.lower() if isinstance(from_temp, str) else None
        
        to_name_lower = to_temp.lower() if isinstance(to_temp, str) else None

        if not (from_name_lower and to_name_lower):
            raise ValueError("Invalid temperature unit. Use 'c'/'f'.")

        # Map aliases: celsius -> Celsius, farhenheit -> Fahrenheit
        
        from_unit_map = {
            "centigrade": "C", 
            "celcius": "C"  # Typo correction for Celcius
            
        }["celsius"] if isinstance(from_temp, str) else None

        to_unit_map = {"fahrenheit": "F"}[to_name_lower] or \
                     {"far": "F"}[to_name_lower]

        
        try:
            celsius_value = value # Assume input is in Celsius unless specified otherwise
            
            if from_temp.lower() == 'c' or ('centigrade' in str(from_temp)):
                celsius_value = float(value)

            elif from_temp.lower() == 'f':
                celsius_value = (float(value) - 32.0) * 5/9 # Convert F to C
            
        except Exception as e:
             print(f"Temperature conversion error for {from_temp} to {to_temp}: {e}")

if __name__ == '__main__':
    pass
