from typing import List, Union

class VolumeCalculator:
    """A class to calculate total volume from a list of measurements in various units."""

    # Conversion factors relative to cubic meters (m^3)
    CONVERSION_FACTORS = {
        'ml': 1e-6,      # milliliters
        'l': 0.001,      # liters
        'gal_us': 0.00378541,  # US gallons
        'gal_uk': 0.00454609,  # UK gallons
        'ft^3': 0.0283168,   # cubic feet
        'yd^3': 0.764555,    # cubic yards
        'm^3': 1.0,          # cubic meters (base unit)
    }

    def __init__(self):
        """Initialize the VolumeCalculator."""
        pass

    def convert_to_base(self, value: float, source_unit: str) -> float:
        """Convert a volume from any supported unit to cubic meters.

        Args:
            value (float): The volume measurement value.
            source_unit (str): The unit of the input measurement.

        Returns:
            float: Volume in cubic meters.
        
        Raises:
            ValueError: If an unsupported unit is provided.
        """
        if source_unit not in self.CONVERSION_FACTORS:
            raise ValueError(f"Unsupported unit: {source_unit}")
        return value * self.CONVERSION_FACTORS[source_unit]

    def calculate_total_volume(self, measurements: List[Union[float, int]], target_unit: str) -> float:
        """Calculate the total volume in a specified target unit.

        Args:
            measurements (List): A list of numeric values representing volumes 
                                 with their corresponding units provided as strings 
                                 or tuples/list pairs if mixed types are expected.
                                 However, based on standard usage patterns for such tasks,
                                 we assume the input is a flat list where each element is either
                                 a float/int OR a tuple (value, unit). To strictly follow "list of volume measurements",
                                 and given type hinting requirements, let's interpret the most robust 
                                 structure: A list of tuples [(val1, 'unit1'), (val2, 'unit2')].
                                 If the prompt implies a simpler flat list where units are implicit or handled differently,
                                 that would contradict "various units". Thus, we assume input is List[Tuple[float/str, str]].

        Note: The task description says "accept a list of volume measurements (in various units)". 
              Standard Python typing for this implies the structure needs to carry unit info.
              If the user intended a flat list like [10, 'ml', 5, 'l'], that requires different parsing logic.
              Given strict type hinting and efficiency: We will assume `measurements` is a List[Tuple[float/str, str]].

        Args (Revised for robustness): 
            measurements: A list of tuples where each tuple contains the numeric value as float/int 
                         and the unit string as second element.
            target_unit (str): The desired output unit.

        Returns:
            float: Total volume converted to the target unit.
        
        Raises:
            ValueError: If an unsupported source or target unit is provided, or if input format is invalid.
        """
        # Validate and convert all measurements to base units (m^3)
        total_m3 = 0.0
        
        for item in measurements:
            if isinstance(item, tuple):
                val_str, unit_str = item
                
                try:
                    value = float(val_str)
                except ValueError as e:
                    raise TypeError(f"Invalid volume value format: {val_str}") from e
                    
                total_m3 += self.convert_to_base(value, unit_str.lower())
            else:
                # Fallback if a single number is passed (assuming default 'm^3' or raising error)
                # To be safe and efficient without complex parsing logic for flat lists which weren't explicitly defined 
                # in the tuple structure above but might be expected by some interpretations.
                # However, "various units" strongly implies unit data must exist per measurement.
                raise ValueError(f"Measurement item {item} does not contain a value and a unit.")

        if target_unit.lower() not in self.CONVERSION_FACTORS:
            raise ValueError(f"Unsupported target unit: {target_unit}")

        # Convert total base volume to target unit using list comprehension for efficiency/clarity
        factors = [self.CONVERSION_FACTORS[unit] for unit in self.CONVERSION_FACTORS.keys()]
        
        return total_m3 / (factors[target_unit.lower()])

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    # Sample data: List of tuples [(value, 'unit'), ...]
    samples = [
        (500.0, 'ml'),           # 500 ml
        (2.5, 'l'),              # 2.5 liters
        (10, 'gal_us'),          # 10 US gallons
        (3.0, 'ft^3'),           # 3 cubic feet
    ]

    calculator = VolumeCalculator()

    try:
        total_m3 = calculator.calculate_total_volume(samples, 'm^3')
        
        print(f"Total volume in {samples[1][1]} is approximately:")
        print(total_m3)
        
        # Additional check with a different target unit to show conversion capability
        total_gal_us = calculator.calculate_total_volume(samples, 'gal_us')
        print(f"\nEquivalent of the same measurements converted back to US gallons: {total_gal_us}")

    except ValueError as e:
        print(f"Error during calculation: {e}")