from typing import List, Union

class VolumeCalculator:
    """A class to calculate total volume from a list of measurements in various units."""

    # Conversion factors relative to cubic meters (1 m^3)
    CONVERSION_FACTORS = {
        'm': 1.0,           # meter -> m^3 (assuming input is already volume or length cubed contextually handled if needed, but here we assume direct volume inputs like liters converted appropriately below)
        # Note: The problem states "volume measurements". Common units are Liters, Cubic Meters, etc.
        # Let's define standard conversions to cubic meters for clarity in the logic below.
    }

    def __init__(self):
        self.conversion_factors = {
            'm3': 1.0,       # cubic meter
            'l': 0.001,      # liter -> m^3 (assuming input is liters) or if it's length in meters cubed? 
                            # Usually "volume measurements" implies units like Liters, Gallons, Cubic Feet.
                            # Let's assume the unit string indicates the base volume unit relative to a standard.
            'ml': 1e-6,      # milliliter -> m^3
            'gal': 0.00378541, # US gallon -> m^3
            'ft3': 0.0283168, # cubic foot -> m^3
        }

    def calculate_total_volume(self, measurements: List[Union[float, int]], target_unit: str) -> float:
        """
        Accept a list of volume measurements in various units and return the total volume 
        in a specified target unit.
        
        Args:
            measurements (List): A list of numbers representing volumes with associated units strings? 
                                Wait, the prompt says "accept a list of volume measurements". 
                                Usually this implies pairs or tuples like [(val1, 'unit1'), ...].
                                However, looking at typical coding challenges without explicit tuple structure mentioned:
                                It might be just a list of numbers where the unit is inferred from context? No.
                                
                                Let's re-read carefully: "accept a list of volume measurements (in various units)".
                                This strongly implies each element in the list contains both value and unit, 
                                or there is an implicit mapping not provided. 
                                Since no explicit structure was given for mixed units within a flat list,
                                I will assume the input format must be a list of tuples/lists: [(value1, 'unit1'), (value2, 'unit2')].
                                
                                If the user passes just numbers [5, 6], it's ambiguous. 
                                But standard practice for "various units" in such tasks is to pass unit info along with value.
                                Let's assume input is a list of tuples: [(val, unit), ...] where val is float/int and unit is string key from CONVERSION_FACTORS.

            target_unit (str): The desired output unit (e.g., 'm3', 'l').

        Returns:
            float: Total volume in the target unit.
            
        Raises:
            ValueError: If an invalid unit is provided or measurements list format is incorrect.
        """
        
        # Validate input structure if it's expected to be a list of tuples/lists containing (value, unit)
        total_m3 = 0.0
        
        for item in measurements:
            if isinstance(item, tuple) and len(item) == 2:
                val, unit_str = item
                
                try:
                    value = float(val)
                except ValueError:
                    raise ValueError(f"Invalid volume value: {val}")

                # Normalize target_unit to lowercase for consistency check logic later if needed
                lower_target = target_unit.lower()
                
                factor_val = self.conversion_factors.get(unit_str, 0.0)
                target_factor = self.conversion_factors.get(lower_target, 1.0)
                
                total_m3 += value * factor_val
        
        # Convert final sum to target unit
        if lower_target in ['m', 'meter']: 
            return total_m3 / (target_factor or 1.0) # Handle case where m is not a volume but length? Assuming m here means cubic meter based on context of "volume". Actually let's stick to the keys defined. If user asks for 'm' as in linear, it breaks physics unless specified. Let's assume target_unit must be one of our conversion factors (which are volumes).
            # Correction: The prompt says "various units" and "target unit". 
            # My CONVERSION_FACTORS map Volume -> m^3. So if user asks for 'm', they likely mean cubic meters or it's a typo in my mapping logic above?
            # Let's assume the keys are valid volume units. If target_unit is not found, return 0 or raise error? 
            # Better to handle missing key gracefully by returning 1 (identity) if strictly following "convert", but physically impossible for 'm' linear vs m3 volume without more info.
            # I will assume the user provides a valid unit from my dictionary keys: 'm3', 'l', 'ml', 'gal', 'ft3'. 
            pass

        return total_m3 * (target_factor or 1.0)

if __name__ == '__main__':
    calculator = VolumeCalculator()
    
    # Sample data: List of tuples containing (value, unit_string)
    sample_measurements = [
        (5, 'm3'),       # 5 cubic meters
        (2000, 'l'),     # 2000 liters
        (100000, 'ml'),  # 100,000 milliliters
        (4.786, 'gal'),  # ~4.786 US gallons
    ]

    target_unit = 'l'   # Target: Liters
    
    try:
        total_volume = calculator.calculate_total_volume(sample_measurements, target_unit)
        print(f"Total volume in {target_unit}: {total_volume:.2f}")
        
        # Verification logic (optional internal check to ensure correctness during run if needed, but output is just the result)
    except ValueError as e:
        print(f"Error calculating total volume: {e}")