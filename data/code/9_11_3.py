import math

class VolumeConverter:
    """
    Optimized class to convert volume between various units using liters as the base unit.
    
    Supported units (abbreviations):
        - ml   : milliliter
        - l    : liter
        - cl   : centiliter
        - dl   : deciliter
        - hL   : hectoliter
        - m3   : cubic meter
    
    Conversion factors relative to liters:
        1 ml = 0.001 L
        1 l  = 1 L
        1 cl = 0.01 L
        1 dl = 0.1 L
        1 hL = 100 L
        1 m3 = 1000 L
    
    The class handles conversion from any supported unit to liters and vice versa,
    ensuring high efficiency through direct multiplication/division without repeated lookups.
    """

    def __init__(self):
        # Predefined factors relative to base unit (liters)
        self._factors = {
            'ml': 0.001,
            'l': 1.0,
            'cl': 0.01,
            'dl': 0.1,
            'hL': 100.0,
            'm3': 1000.0
        }

    def _validate_unit(self, unit):
        """Check if the provided unit is supported."""
        return unit.lower() in self._factors

    def to_base_unit(self, value: float, from_unit: str) -> float:
        """Convert a volume from any supported unit to liters (base unit)."""
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be an integer or float.")
        
        lower_unit = from_unit.lower()
        if not self._validate_unit(lower_unit):
            raise ValueError(f"Unsupported volume unit: {from_unit}. Supported units are ml, l, cl, dl, hL, m3.")

        return value * self._factors[lower_unit]

    def to_other_unit(self, value: float, from_unit: str, to_unit: str) -> float:
        """Convert a volume from one supported unit to another."""
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be an integer or float.")
        
        lower_from = from_unit.lower()
        lower_to = to_unit.lower()

        if not self._validate_unit(lower_from) or not self._validate_unit(lower_to):
            raise ValueError(f"Unsupported volume unit(s). Supported units are ml, l, cl, dl, hL, m3.")

        # Convert from source to base (liters), then to target
        liters = value * self._factors[lower_from]
        return liters / self._factors[lower_to]

if __name__ == '__main__':
    converter = VolumeConverter()

    # Sample conversions demonstrating functionality without user input or external dependencies
    
    # Convert 500 ml to liters
    result_1 = converter.to_base_unit(500, 'ml')
    
    # Convert 2.5 m3 to liters
    result_2 = converter.to_base_unit(2.5, 'm3')
    
    # Convert 1 liter back to milliliters (liters -> ml)
    result_3 = converter.to_other_unit(result_2, 'l', 'ml')
    
    # Convert 0.5 hL to deciliters (hL -> dl)
    result_4 = converter.to_other_unit(0.5, 'hL', 'dl')

    print(f"Converted {result_1} liters from 500 ml")
    print(f"Converted {result_2} liters from 2.5 m3")
    print(f"Converted {result_3} milliliters from the previous result in liters")
    print(f"Converted {result_4} deciliters from 0.5 hL")

    # Additional test case: direct conversion between non-base units (cl -> dl)
    cl_value = 125
    dl_result = converter.to_other_unit(cl_value, 'cl', 'dl')
    print(f"Converted {dl_result} deciliters from {cl_value} centiliters")

    # Edge case: zero value
    zero_liters = converter.to_base_unit(0, 'l')
    assert zero_liters == 0.0
    
    # Negative volume (physically possible in some contexts like debt or virtual space)
    neg_ml = -150
    neg_liters = converter.to_base_unit(neg_ml, 'ml')
    print(f"Converted {neg_liters} liters from negative input")

    # Verify factor consistency: 3 cl should be equal to 0.03 L via two steps (cl -> l -> base)
    step1 = converter.to_other_unit(3, 'cl', 'l')
    assert abs(step1 - 0.03) < 1e-9
    
    print("All sample tests passed successfully.")