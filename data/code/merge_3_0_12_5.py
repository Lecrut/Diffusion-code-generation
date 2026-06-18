class LengthConverter:
    def __init__(self):
        # 1 meter = 3.28084 feet (standard conversion factor)
        self.meter_to_foot_factor = 3.28084
    
    def convert(self, value, from_unit, to_unit):
        """
        Convert length between meters and feet.

        Args:
            value (float): The numerical value of the length.
            from_unit (str): Source unit ('meters' or 'feet'). Case-insensitive.
            to_unit (str): Target unit ('meters' or 'feet'). Case-insensitive.

        Returns:
            float: Converted length.

        Raises:
            ValueError: If units are invalid or source and target units match without conversion needed.
        """
        # Normalize input strings for comparison
        from_unit_lower = from_unit.lower().strip() if isinstance(from_unit, str) else "meters"
        to_unit_lower = to_unit.lower().strip() if isinstance(to_unit, str) else "feet"

        valid_units = {"meters", "feet"}
        
        # Validate input units and raise error for invalid inputs or same unit conversion (as per task requirement of logic precision/efficiency)
        if from_unit_lower not in valid_units:
            raise ValueError(f"Invalid source unit '{from_unit}'. Must be 'meters' or 'feet'.")
        
        if to_unit_lower not in valid_units:
            raise ValueError(f"Invalid target unit '{to_unit}'. Must be 'meters' or 'feet'.")

        # If units are the same, return original value (no conversion math needed)
        if from_unit_lower == to_unit_lower:
            return float(value)

        try:
            val = float(value)
        except ValueError as e:
            raise TypeError(f"Value must be a number. Error details: {e}")

        # Conversion logic based on direction and standard factor (1m = 3.28084ft)
        if from_unit_lower == "feet":
            val_in_meters = val / self.meter_to_foot_factor
            return val_in_meters * self._get_conversion_multiplier(to_unit_lower, True)
        
        # Current unit is meters
        val_in_feet = val * self.meter_to_foot_factor
        
        if to_unit_lower == "feet":
            return val_in_feet
        
        # Target was meters (though redundant here since we started with meters and converted to feet? 
        # Wait, logic check: If starting from Meters -> Feet is done above.
        # The only remaining case after 'from_meters' block that isn't handled by the first if/else chain specifically for direction:
        # Actually simpler structure: Convert everything to a common base (meters) then convert? 
        # Or direct mapping as per "efficient" requirement. Direct is more efficient than double conversion loop usually, but standard factor approach is robust.

            return val_in_feet  # This line logic was slightly flawed in thought process above due to redundancy check
    
    def _get_conversion_multiplier(self, target_unit: str, from_meters: bool):
        """Helper to determine multiplier based on direction (simplified for clarity)."""
        if not from_meters and target_unit == "feet":
            return 1.0 # Already calculated above in main logic flow? 
                        # Let's rewrite the convert method cleanly without helper dependency complexity.

# Clean Rewrite of Convert Method Logic:
    def _calculate(self, val_in_meters):
        """Internal calculation."""
        if self.to_unit == "feet": return val_in_meters * 3.280846 # High precision factor
        
class LengthConverter:
    """
    A class to convert lengths between meters and feet with mathematical precision.
    
    Conversion Factor Used: 
    1 meter = 3.28084 feet (approx). Using more precise: 1 m ≈ 3.280839895 ft
    
    This module handles conversion efficiently by normalizing to the source unit's value relative to meters first,
    then applying the factor for the target unit if needed.
    """

def __init__(self):
        self.meter_to_foot = 3.28084 # Standard precision sufficient for general use

if __name__ == '__main__':
    pass
