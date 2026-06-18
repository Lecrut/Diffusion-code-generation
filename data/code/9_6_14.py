class VolumeConversionSystem:
    """A dictionary-based system for mapping volume conversion factors."""

    def __init__(self):
        # Base unit is liters (L). All other units will be converted to L, then back to target.
        self._base_unit = "liter"
        
        # Map each known unit to its value in the base unit (liters) and a human-readable name.
        # Format: {unit_name: {"factor_to_base": float, "display_name": str}}
        self._conversion_factors = {
            "liter": {"factor_to_base": 1.0, "display_name": "Liter"},
            "milliliter": {"factor_to_base": 0.001, "display_name": "Milliliter (ml)"},
            "kiloliter": {"factor_to_base": 1000.0, "display_name": "Kiloliter"},
            "cubic_meter": {"factor_to_base": 1000.0, "display_name": "Cubic Meter (m³)"},
            "gallon_us": {"factor_to_base": 3.785411784, "display_name": "US Fluid Gallon"},
            "gallon_uk": {"factor_to_base": 4.54609, "display_name": "Imperial Gallon (UK)"},
            "fluid_ounce_us": {"factor_to_base": 0.0295735295625, "display_name": "US Fluid Ounce"},
            "pint_us": {"factor_to_base": 0.473176473, "display_name": "US Pint"},
            "quart_us": {"factor_to_base": 0.946352946, "display_name": "US Quart"},
            "gallon_imperial": {"factor_to_base": 4.54609, "display_name": "Imperial Gallon (UK)"}, # Duplicate key logic handled by dict update or separate entry if needed; here using alias for clarity in demo
        }

    def _normalize_unit(self, unit_str):
        """Normalize input string to a standard dictionary key."""
        return unit_str.strip().lower()

    def convert_from_to(self, amount: float, from_unit: str, to_unit: str) -> float:
        """
        Convert an amount from one volume unit to another.
        
        Logic is decoupled via the _conversion_factors dictionary mapping everything 
        relative to the base unit (liter).
        
        Steps:
        1. Normalize input strings.
        2. Retrieve factors for source and target units. If a factor doesn't exist, raise an error.
        3. Convert amount from 'from_unit' to 'base_unit'.
        4. Convert amount from 'base_unit' to 'to_unit'.
        
        Args:
            amount (float): The value to convert.
            from_unit (str): Source unit name.
            to_unit (str): Target unit name.
            
        Returns:
            float: Converted value in the target unit.
            
        Raises:
            ValueError: If units are not recognized or factor is missing.
        """
        normalized_from = self._normalize_unit(from_unit)
        normalized_to = self._normalize_unit(to_unit)

        if normalized_from not in self._conversion_factors:
            raise ValueError(f"Unsupported conversion unit: {from_unit}")
        
        if normalized_to not in self._conversion_factors:
            # Check for common aliases like 'gal' -> 'gallon_us', etc. could be added here, 
            # but strictly following the dict keys defined above ensures safety against typos.
            raise ValueError(f"Unsupported conversion unit: {to_unit}")

        factor_from = self._conversion_factors[normalized_from]["factor_to_base"]
        factor_to = self._conversion_factors[normalized_to]["factor_to_base"]

        # Convert to base (liters) then to target
        amount_in_base = amount * factor_from
        result_amount = amount_in_base / factor_to
        
        return result_amount

if __name__ == '__main__':
    system = VolumeConversionSystem()

    # Sample conversions with hard-coded values
    samples = [
        ("1", "liter", "milliliter"),          # 1 L -> ml
        ("2.5", "gallon_us", "quart_us"),     # 2.5 US gal -> qt
        (0, "cubic_meter", "liters"),         # 0 m³ -> L
        ("-5", "pint_us", "fluid_ounce_us"),  # -5 pt -> fl oz
    ]

    print("Volume Conversion System Demo")
    print("-" * 30)

    for amount_str, from_unit_name, to_unit_name in samples:
        try:
            result = system.convert_from_to(float(amount_str), from_unit_name, to_unit_name)
            # Retrieve display names for cleaner output if available (optional enhancement)
            factor_info_from = system._conversion_factors.get(from_unit_name.lower()) or {}
            factor_info_to = system._conversion_factors.get(to_unit_name.lower()) or {}
            
            print(f"Input: {amount_str} {from_unit_name}")
            print(f"Output: {result:.4f} {to_unit_name}")
        except ValueError as e:
            print(f"Error processing '{amount_str}' from {from_unit_name}: {e}")

    # Additional complex factor check demonstration (Decoupled Logic)
    # We do not store the direct 1 m³ = X gal relationship; it is derived via Liters.
    test_case_m3_to_gal_us = system.convert_from_to(1, "cubic_meter", "gallon_us")
    print("-" * 30)
    print(f"Demonstrating decoupled logic: 1 m³ to US Gallons")
    print(f"Result: {test_case_m3_to_gal_us:.4f} gallons (derived via Liters, not hardcoded direct factor)")