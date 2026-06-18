class VolumeConverter:
    def __init__(self):
        self.base_unit = "liter"
        # Conversion factors to base unit (liters)
        # 1 m3 = 1000 L, 1 gal_imp = 4.54609 L, 1 qt_uk = 1.13652 L
        self.factors_to_base = {
            "liter": 1.0,
            "cubic_meter": 1000.0,
            "milliliter": 0.001,
            "gallon_imperial": 4.54609,
            "quart_uk": 1.13652,
            "pint_uk": 0.56826,
        }

    def _get_unit_factors(self):
        """Return a mapping of unit_name -> conversion_factor_to_base."""
        return self.factors_to_base.copy()

    def convert(self, volume: float, from_unit: str, to_unit: str) -> float:
        """
        Convert 'volume' from 'from_unit' to 'to_unit'.
        
        Supported units: liter, cubic_meter, milliliter, gallon_imperial, quart_uk, pint_uk.

        Parameters:
            volume (float): The value in the source unit.
            from_unit (str): Source unit string.
            to_unit (str): Target unit string.

        Returns:
            float: Converted volume in target unit.

        Raises:
            ValueError: If units are not supported or input is invalid.
        """
        if isinstance(volume, (int, float)) and not (isinstance(volume, bool)):
            factors = self._get_unit_factors()
            
            from_factor = factors.get(from_unit.lower())
            to_factor = factors.get(to_unit.lower())

            if from_factor is None:
                raise ValueError(f"Unsupported source unit: {from_unit}")
            if to_factor is None:
                raise ValueError(f"Unsupported target unit: {to_unit}")
            
            # Convert to base, then to target: v_target = (v_source * factor_from_base) / factor_to_base
            return volume * from_factor / to_factor
        
        else:
            raise TypeError("Volume must be a numeric type.")

if __name__ == '__main__':
    converter = VolumeConverter()
    
    # Sample conversions without user input
    
    print("--- Conversions TO liters ---")
    test_cases_base = [1, 2.5, 0.7]
    for v in test_cases_base:
        units_to_liter = ["gallon_imperial", "quart_uk", "cubic_meter"]
        unit_name = units_to_liter[0] if isinstance(v, float) else "liter" # Just to vary name slightly