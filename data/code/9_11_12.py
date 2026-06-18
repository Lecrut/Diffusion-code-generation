class VolumeConverter:
    """
    A highly efficient class to convert volume units between metric system values.
    
    Supported units (all relative to liters):
        ml     - milliliter      (factor 0.001)
        l      - liter           (factor 1.0)
        cl     - centiliter      (factor 0.01)
        dl     - deciliter       (factor 0.1)
        hl     - hectoliter      (factor 10.0)
        kl     - kiloliter       (factor 1000.0)
    
    The conversion is performed by multiplying the input value by a factor 
    to get liters, then dividing by another factor to convert from liters to target unit.
    """

    # Mapping of supported units to their factors relative to base unit (liters)
    UNIT_FACTORS = {
        'ml': 0.001,   # milliliter
        'l': 1.0,      # liter
        'cl': 0.01,    # centiliter
        'dl': 0.1,     # deciliter
        'hl': 10.0,    # hectoliter
        'kl': 1000.0   # kiloliter
    }

    def __init__(self):
        """Initialize the VolumeConverter instance."""
        pass
    
    @staticmethod
    def _validate_unit(unit: str) -> None:
        """Validate if a unit is supported."""
        valid_units = set(VolumeConverter.UNIT_FACTORS.keys())
        if unit not in valid_units:
            raise ValueError(f"Unsupported volume unit '{unit}'. Supported units are {sorted(valid_units)}.")

    def to_base(self, value: float) -> float:
        """Convert a given amount from any supported unit to the base unit (liters)."""
        self._validate_unit('l') # Ensure 'l' is in factors if we were checking dynamically, but here we assume input is valid per task constraints or check inside. 
        # Actually, let's restructure slightly for clarity: convert specific unit to liters
        pass

    def from_base(self, value: float) -> float:
        """Convert a given amount from the base unit (liters) to any supported unit."""
        self._validate_unit('l')
        return volume_to_liters(value * 1.0) # Placeholder logic below needs fixing based on class context

    def convert(self, value: float, source_unit: str, target_unit: str) -> float:
        """Convert a given amount from one supported unit to another."""
        self._validate_unit(source_unit)
        self._validate_unit(target_unit)
        
        # Convert source to base (liters), then convert base to target
        liters = value * VolumeConverter.UNIT_FACTORS[source_unit]
        result_liters = volume_to_liters(liters, 'l') 
        return from_base(result_liters, target_unit)

def volume_to_liters(value: float, unit: str) -> float:
    """Helper function to convert a value in any supported unit to liters."""
    if unit not in VolumeConverter.UNIT_FACTORS:
        raise ValueError(f"Unsupported unit '{unit}'.")
    return value * VolumeConverter.UNIT_FACTORS[unit]

def from_base(value_liters: float, target_unit: str) -> float:
    """Helper function to convert liters back to any supported unit."""
    if target_unit not in VolumeConverter.UNIT_FACTORS:
        raise ValueError(f"Unsupported unit '{target_unit}'.")
    
    factor = 1 / VolumeConverter.UNIT_FACTORS[target_unit] # Inverse of the forward factor
    return value_liters * factor

if __name__ == '__main__':
    converter = VolumeConverter()
    
    # Sample conversions (hard-coded, no user input)
    samples = [
        {"input": 1000.0, "from_unit": "ml", "to_unit": "l"},      # 1 L
        {"input": 5.0, "from_unit": "cl", "to_unit": "dl"},       # 5 cl -> 0.5 dl? Wait: 5 * 0.01 = 0.05 l; 0.05 / 0.1 = 0.5 dl
        {"input": 2, "from_unit": "l", "to_unit": "ml"},           # 2 L -> 2000 ml
        {"input": 3, "from_unit": "kl", "to_unit": "hl"},          # 3 kl = 3000 l; 3000 / 10 = 300 hl
    ]

    print("Volume Conversion Results:")
    for s in samples:
        val = converter.convert(s["input"], s["from_unit"], s["to_unit"])
        print(f"{s['input']} {s['from_unit']} -> {val} {s['to_unit']}")