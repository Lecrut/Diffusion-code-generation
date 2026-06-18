import math

class VolumeConverter:
    """A class to handle volume conversions using a dictionary-based system."""
    
    def __init__(self):
        # Base unit is cubic meters (m³). All other units are defined relative to m³.
        self._base_unit = "m3"
        
        # Mapping of all required conversion factors from base unit (m³) to each target unit.
        # Value represents: 1 <target_unit> = X * 1_base_unit
        self._conversion_factors = {
            "ml": 0.001,           # 1 ml = 0.001 m³
            "l": 0.001,           # 1 L = 0.001 m³ (Note: Liter is defined as exactly 0.001 cubic meters)
            "gal_us": 3785411.784,   # 1 US gallon ≈ 3785411.784 ml = ... wait, let's re-calculate relative to m³ directly for precision.
        }
        
        # Correction: Let's define factors as "value in base unit (m³) per one target unit".
        # So if I have 1 gallon, how many m³ is it? Or conversely, what factor converts input volume of type T to output volume of type B.
        # Standard approach for decoupled logic: 
        # Define a dictionary where keys are units and values are the number of base_units in one unit_of_key.
        # E.g., 1 m3 = 1 * m3_base => factor is 1.0
        #      1 l   = 0.001 * m3_base => factor is 0.001
        
        self._factors_from_base = {
            "m3": 1.0,
            "ml": 1e-6,           # 1 ml = 0.000001 m³ (Correction: Liter = cubic decimeter. 1 L = 0.001 m^3. 1 ml = 1e-6 m^3)
            "l": 1e-3,            # 1 L = 0.001 m³
            "gal_us": 2834795.747,   # Wait, this is wrong direction. 
        }

    def __init__(self):
        """Initialize the converter with precise conversion factors relative to cubic meters (m³)."""
        self._base_unit = "m3"
        
        # Dictionary mapping unit names to their value in terms of 1 base_unit (cubic meter).
        # This ensures logic is decoupled from constants. To convert A -> B: 
        # result(A) * factors[A] / factors[B]

if __name__ == '__main__':
    pass
