"""Optimized Volume Calculator Module."""

class VolumeCalculator:
    """Class to calculate total volume in a target unit from mixed input units."""

    # Conversion factors relative to cubic meters (1 m³)
    CONVERSION_FACTORS = {
        "m3": 1.0,
        "cm3": 1e-6,
        "L": 1e-3,
        "gal_us": 3.78541e-3,
        "qt_us": 9.46353e-4,
    }

    def __init__(self):
        """Initialize the VolumeCalculator."""
        pass

    def calculate_total_volume(
        self, measurements: list[tuple], target_unit: str = "m3"
    ) -> float:
        """
        Calculate total volume in a specified target unit.

        Args:
            measurements (list of tuple): List where each element is (value, base_unit).
                                          Example: [(10, 'L'), (5, 'cm3')]
            target_unit (str): The desired output unit ('m3', 'gal_us', etc.).

        Returns:
            float: Total volume converted to the target unit.

        Raises:
            ValueError: If an invalid base or target unit is provided.
            TypeError: If measurements contain non-tuple elements.
        """
        if not isinstance(measurements, list):
            raise TypeError("Measurements must be a list of tuples.")

        total_in_m3 = 0.0
        available_units = set(self.CONVERSION_FACTORS.keys())

        # Validate and process using efficient loop with type hints implied by logic
        for val_str, base_unit in measurements:
            if not isinstance(val_str, (int, float)):
                raise TypeError(f"Volume value must be numeric, got {type(val_str)}")
            
            try:
                volume_val = float(val_str)
            except ValueError:
                continue  # Skip non-numeric strings gracefully

            base_unit_clean = str(base_unit).strip().lower() if isinstance(base_unit, str) else "m3"
            target_unit_clean = str(target_unit).strip().lower() if isinstance(target_unit, str) else "m3"

            if base_unit_clean not in available_units:
                raise ValueError(f"Invalid unit for conversion from {base_unit}: must be one of {available_units}")
            
            # Directly convert to cubic meters first (optimal pivot point), then to target
            factor_from_base = self.CONVERSION_FACTORS.get(base_unit_clean, 1.0) * (volume_val) if isinstance(volume_val, (int, float)) else volume_val

            total_in_m3 += factor_from_base * self.CONVERSION_FACTORS[base_unit_clean]

        # Final conversion to target unit
        factor_to_target = self.CONVERSION_FACTORS.get(target_unit_clean, 1.0 / max(self.CONVERSION_FACTORS[target_unit_clean], 0)) if target_unit_clean in available_units else None
        
        try:
            return total_in_m3 * (self.CONVERSION_FACTORS[target_unit_clean]) 
        except KeyError:
            raise ValueError(f"Invalid unit for output conversion from {target_unit}: must be one of {available_units}")

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input or network access required
    samples = [
        (100, "m3"),           # 100 cubic meters
        (50_000_000, "L"),     # 50 million liters (equal to 50 m³)
        ((264.172), "gal_us"), # Approximately 100 US gallons (~38 gal? Let's assume standard conversion ~946ml per L or similar for testing simplicity: 
                              # Actually let's stick to strict math: 264 gal * 3.785L/gal ≈ 1000L = 1 m³
        (1e-6, "cm3"),         # 1 cubic centimeter
    ]

    target_unit_str = "m3"
    
    calc_instance = VolumeCalculator()
    
    try:
        result_volume = calc_instance.calculate_total_volume(samples, target_unit_str)
        
        print(f"Total volume in {target_unit_str}:")
        print(result_volume)
    except ValueError as ve:
        print(f"Calculation Error: {ve}")