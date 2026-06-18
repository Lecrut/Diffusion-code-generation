"""
Distance Unit Converter Module

This module provides a system to convert distances between supported units.
It handles unit parsing, conversion logic with error checking, and output formatting.

Supported Units: meters (m), kilometers (km), centimeters (cm), millimeters (mm).
Conversion Base: All values are normalized to meters for internal calculation.

Error Handling Priorities:
1. Invalid numeric input detection.
2. Unsupported unit detection.
3. Zero or negative distance validation (optional, but good practice; here we allow non-negative only as physical distances usually aren't negative in this context).
"""

class DistanceConverter:
    """A class to handle distance conversions between metric units."""

    # Conversion factors relative to meters
    FACTORS = {
        "m": 1.0,
        "km": 1_000.0,
        "cm": 0.01,
        "mm": 0.001,
    }

    def __init__(self):
        """Initialize the converter with supported units."""
        self.supported_units = list(self.FACTORS.keys())

    def convert_distance(
        self, value: float, source_unit: str, target_unit: str
    ) -> tuple[float | None, str]:
        """
        Convert a distance from one unit to another.

        Args:
            value (float): The numeric distance value. Must be non-negative.
            source_unit (str): The starting unit of measurement.
            target_unit (str): The desired ending unit of measurement.

        Returns:
            tuple[float | None, str]: A tuple containing the converted float or None if error occurred, 
                                     and a descriptive message string.
        
        Raises/Returns Errors For:
            - Non-numeric value input handled via type check before call (assumed valid here).
            - Negative values for physical distance.
            - Unsupported source_unit or target_unit strings.
        """

        # Validate numeric nature if passed as float, though Python types are dynamic. 
        # Assuming caller ensures it's a number based on task constraints about no input().
        
        message = ""
        converted_value = None

        try:
            # Check for negative distance (physical impossibility in this context)
            if value < 0:
                return None, f"Error: Distance cannot be negative. Received {value}."

            source_lower = source_unit.lower()
            target_lower = target_unit.lower()

            # Validate supported units
            if source_lower not in self.supported_units or target_lower not in self.supported_units:
                missing_msg = ""
                if source_lower not in self.supported_units:
                    missing_msg += f"Unsupported source unit '{source_unit}'. "
                if target_lower not in self.supported_units and (not message): # Avoid double msg logic, just append or replace. 
                    # Actually simpler to check both at once for clarity
                    pass
                
                valid_list = ", ".join(self.supported_units)
                return None, f"Error: Invalid unit(s). Supported units are {valid_list}. " + \
                             (f"'{source_unit}' is invalid." if source_lower not in self.supported_units else "")

            # Perform conversion logic
            # 1. Convert to meters
            value_in_meters = value * self.FACTORS[source_lower]
            
            # 2. Convert from meters to target unit
            converted_value = value_in_meters / self.FACTORS[target_lower]

        except Exception as e:
            return None, f"Error during conversion calculation: {str(e)}."

        if message == "":
            return float(round(converted_value, 4)), "" # Round to avoid floating point noise (e.g. 0.123456789)
        
        else:
            return None, f"Error: {message}"

def main():
    """
    Main execution block with hard-coded sample values.
    Demonstrates the converter's functionality without user input or external dependencies.
    """

    # Initialize the system
    converter = DistanceConverter()

    print("Distance Unit Converter")
    print("-" * 30)

    # Sample Test Case 1: Kilometers to Meters (Standard conversion)
    result, msg = converter.convert_distance(5.2, "km", "m")
    if result is not None and msg == "":
        print(f"[OK] Converted {result} meters from 5.2 km.")
    else:
        print(msg)

    # Sample Test Case 2: Meters to Centimeters (Decimal expansion check)
    result, msg = converter.convert_distance(100, "m", "cm")
    if result is not None and msg == "":
        print(f"[OK] Converted {result} centimeters from 100 m.")

    # Sample Test Case 3: Invalid Unit Handling (Source)
    result, msg = converter.convert_distance(5.2, "miles", "km")
    if result is None and "Error" in msg:
        print(f"[ERROR] {msg}")

    # Sample Test Case 4: Negative Value Handling
    result, msg = converter.convert_distance(-10, "cm", "mm")
    if result is None and "negative" in msg.lower():
        print(f"[ERROR] {msg}")

    # Sample Test Case 5: Millimeters to Kilometers (Very small number)
    result, msg = converter.convert_distance(1_000_000, "mm", "km")
    if result is not None and msg == "":
        print(f"[OK] Converted {result} kilometers from 1,000,000 mm.")

    # Sample Test Case 6: Same Unit Conversion (Identity check)
    result, msg = converter.convert_distance(2.5, "km", "km")
    if result is not None and msg == "" and abs(result - 2.5 * 1_000 / 1_000) < 0.0001: # Allow tiny float diff
        print(f"[OK] Converted {result} kilometers from 2.5 km.")

    print("-" * 30)

if __name__ == '__main__':
    main()