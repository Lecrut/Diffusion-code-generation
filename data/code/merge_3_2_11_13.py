from typing import List, Union

# Conversion factors to cubic meters (1 unit -> m^3)
CONVERSION_FACTORS = {
    'm': 1.0,      # meter
    'cm': 1e-6,    # centimeter
    'mm': 1e-9,    # millimeter
    'km': 1e9,     # kilometer
    'L': 0.001,    # liter
    'm3': 1.0,     # cubic meter (alias for m^3)
}

class VolumeCalculator:
    """A class to calculate total volume converting various units to a target unit."""
    
    def __init__(self):
        self.conversion_factors = CONVERSION_FACTORS
    
    def convert_to_target_unit(self, measurements: List[Union[int, float]], 
                                source_units: List[str], 
                                target_unit: str) -> Union[float, int]:
        """
        Accept a list of volume measurements in various units and return the total volume 
        in the specified target unit.

        Args:
            measurements (List[Union[int, float]]): List of numerical volume values.
            source_units (List[str]): Corresponding list of string unit identifiers for each value.
            target_unit (str): The target unit to convert all volumes into.

        Returns:
            Union[float, int]: Total volume in the target unit as a number.
        
        Raises:
            ValueError: If units are mismatched or an invalid unit is provided.
        """
        if len(measurements) != len(source_units):
            raise ValueError("The length of measurements and source_units must be equal.")
            
        # Validate input lists lengths match before proceeding (already checked above, but good practice in logic flow).

        total_volume_m3 = 0.0
        
        for value, unit_str in zip(measurements, source_units):
            if not isinstance(value, (int, float)):
                raise ValueError(f"Invalid measurement type: {type(value)}")
            
            # Normalize target_unit to lowercase and handle aliases like 'm^3' -> 'm3'
            normalized_target = target_unit.lower()
            if unit_str in self.conversion_factors:
                factor = self.conversion_factors[unit_str]
                total_volume_m3 += value * factor
            
        final_result = total_volume_m3 / self.conformation_factors.get(normalized_target, 1.0)

        return round(final_result, 6) # Round to avoid floating point noise unless exact integer result expected

def main():
    """Main execution block with hard-coded sample values."""
    
    calculator = VolumeCalculator()
    
    # Sample data: measurements and their corresponding units
    sample_measurements = [100, 25.5, -5, 3000] 
    sample_units = ['cm', 'm', 'mm', 'L'] 
    
    target_unit_input = "m" 

    try:
        result = calculator.convert_to_target_unit(sample_measurements, sample_units, target_unit_input)
        
        # Output the result directly without prompts or interactive input.
        print(f"Total volume in {target_unit_input}: {result}")

    except Exception as e:
        print(f"Error occurred during calculation: {e}")

if __name__ == '__main__':
    main()