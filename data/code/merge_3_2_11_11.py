from typing import List, Union

class VolumeCalculator:
    """A class to calculate total volume from mixed units."""

    # Conversion factors relative to cubic meters (m^3)
    CONVERSION_FACTORS = {
        'ml': 1e-6,      # milliliters
        'l': 0.001,      # liters
        'gal_us': 3.78541e-3,  # US gallons
        'gal_uk': 4.54609e-3,  # UK gallons
        'ft^3': 2.83168e-2,    # cubic feet
        'yd^3': 7.64555e-2,    # cubic yards
        'm^3': 1.0,            # cubic meters (base unit)
    }

    def __init__(self):
        """Initialize the VolumeCalculator."""
        pass

    def calculate_total_volume(
        self, 
        measurements: List[Union[int, float]], 
        target_unit: str = 'm^3'
    ) -> Union[float, int]:
        """
        Calculate the total volume from a list of measurements in various units.

        Args:
            measurements (List[Union[int, float]]): A list of volumes with their corresponding unit strings appended. 
                Format expected as [value1_unit1, value2_unit2, ...]. Example: [[50, 'ml'], [2, 'l']].
            target_unit (str): The unit to convert the total volume into. Default is cubic meters ('m^3').

        Returns:
            Union[float, int]: Total volume in the specified target unit.

        Raises:
            ValueError: If an unsupported unit is provided or if measurements list format is incorrect.
        """
        # Validate and process input using efficient list comprehension to convert everything to base units (m^3)
        total_m3 = 0.0
        
        for item in measurements:
            value, unit_str = self._parse_item(item)
            
            if not isinstance(value, (int, float)):
                raise ValueError(f"Invalid volume value type: {type(value).__name__}")
                
            # Convert to base units using dictionary lookup with default handling via get() and explicit check for safety
            factor = self.CONVERSION_FACTORS.get(unit_str.lower())
            
            if factor is None:
                raise ValueError(f"Unsupported unit '{unit_str}'. Supported units are {list(self.CONVERSION_FACTORS.keys())}")
                
            total_m3 += value * factor

        # Convert the final result to the target unit using efficient list comprehension logic (single lookup)
        target_factor = self.CONVERSION_FACTORS.get(target_unit.lower(), 1.0 / self.CONVERSION_FACTORS['m^3']) if 'm^3' in self.CONUTION_FACTORS else None
        
        # Re-calculate factor for safety against typo in CONVERSION_FACTORS keys during runtime logic flow
        target_factor = self.CONVERSION_FACTORS.get(target_unit.lower()) or 1.0

        return total_m3 * (1 / target_factor) if target_factor > 0 else float('inf')

    def _parse_item(self, item: Union[int, float]) -> tuple:
        """Helper to parse a measurement list element assuming format [value, unit]."""
        # Assuming the input is passed as a flat list of tuples or lists internally for this specific task requirement 
        # OR if the user passes a structure like [[val1, 'unit1'], [val2, 'unit2']] which matches typical mixed-unit scenarios.
        # However, to strictly follow "accept a list of volume measurements", we assume the input is already structured correctly 
        # as per common practice in such tasks: each element is (value, unit).
        
        if isinstance(item, tuple) and len(item) == 2:
            return item[0], str(item[1])
        elif isinstance(item, list) and len(item) >= 2:
            try:
                val = float(item[0])
                unit_str = str(item[1]).lower() if hasattr(item[1], '__str__') else 'm^3' # Fallback to m^3 if string conversion fails on weird types
                return val, unit_str
            except (ValueError, TypeError):
                 raise ValueError(f"Invalid measurement format: {item}")
        elif isinstance(item, (int, float)):
             # If only a number is passed without explicit unit context in the list structure provided by user logic 
             # we might assume it's m^3 or throw error. Given task constraints on "various units", 
             # let's assume if single value comes through as raw int/float in this specific helper call,
             # but looking at main usage pattern: usually users pass [[50,'ml'], [2,'l']].
             return item, 'm^3'
        else:
            raise ValueError(f"Unsupported measurement format type: {type(item)}")

if __name__ == '__main__':
    # Hard-coded sample values running without user input or network access.
    calculator = VolumeCalculator()

    # Sample data: List of [value, unit] tuples representing mixed volume measurements
    samples = [
        [[50, 'ml'],      # 50 milliliters
         [2, 'l'],        # 2 liters
         [1.5, 'gal_us'], # 1.5 US gallons
         [3, 'ft^3'],     # 3 cubic feet
         [0.1, 'm^3']]    # 0.1 cubic meters
    ]

    try:
        total = calculator.calculate_total_volume(samples)
        print(f"Total volume in m^3: {total}")
        
        # Demonstrate conversion to another unit (e.g., liters) if needed by re-calling or modifying logic, 
        # but the method returns based on target_unit argument. Let's show result for 'l' as well conceptually 
        # though we only print one execution here per run constraint unless looped.
        
    except ValueError as e:
        print(f"Error calculating volume: {e}")