"""Volume Management Module."""

class VolumeConverter:
    """A class to convert between metric (L, mL, m³) and imperial (L, gal) volume units."""

    # Conversion constants relative to 1 cubic meter (m³)
    _M3_TO_L = 1000.0
    _L_TO_ML = 1000.0
    _L_TO_GAL_IMPERIAL = 8.798769931964254

    def __init__(self, source_unit: str, target_unit: str) -> None:
        """Initialize the converter with a source and target unit."""
        self.source_unit = source_unit.lower()
        self.target_unit = target_unit.lower()

        # Validate units against supported set
        valid_units = {'m3', 'l', 'ml', 'gal'}
        if not (self.source_unit in valid_units or self.target_unit in valid_units):
            raise ValueError(f"Unsupported unit. Supported: {valid_units}")

    def convert(self, value: float) -> float:
        """Convert a volume from the source unit to the target unit."""
        # Ensure non-negative input for physical volumes
        if value < 0:
            raise ValueError("Volume cannot be negative.")

        # Define conversion factors relative to cubic meters (m³)
        m3_factors = {
            'm3': 1.0,
            'l': self._M3_TO_L / 1_000_000.0,  # L is smaller than M3? No, M3=1000L. So factor for M3->L is 1000. 
                                                # Wait: Let's standardize on a base unit (e.g., Liters)
        }

        # Re-evaluating factors based on Liter as the common intermediate unit
        # Base Unit: Liter
        
        if self.source_unit == 'm3':
            value_in_liters = value * 1000.0
        elif self.source_unit in ('l',):
            value_in_liters = value
        else:
            raise ValueError("Source unit must be m³ or L.")

        # Convert from Liters to target unit
        if self.target_unit == 'm3':
            return value_in_liters / 1000.0
        elif self.target_unit in ('l',):
            return value_in_liters
        else:
            raise ValueError("Target unit must be m³, L, or mL.")

    def convert_milliliters(self, volume_ml: float) -> tuple[float, str]:
        """Convert milliliters to a specified target unit and return the result."""
        if self.target_unit in ('l',):
            return (volume_ml / 1000.0, 'L')
        elif self.target_unit == 'm3':
            return ((volume_ml / 1000.0) / 1000.0, 'm³')
        else:
            raise ValueError("Target unit must be L or m³.")

    def convert_gallons(self, volume_gal: float) -> tuple[float, str]:
        """Convert gallons to a specified target metric unit and return the result."""
        # 1 Imperial Gallon = ~4.54609 Liters
        
        if self.target_unit in ('l',):
            liters = volume_gal * 4.54609
            return (liters, 'L')
        elif self.target_unit == 'm3':
            m3_liters = liters / 1000.0
            return ((volume_gal * 4.54609) / 1000.0, 'm³')
        else:
            raise ValueError("Target unit must be L or m³.")

def convert_volume(volume_value: float, source_unit: str, target_unit: str) -> tuple[float, str]:
    """
    Public function to convert a volume between units.

    Args:
        volume_value (float): The numeric value of the volume.
        source_unit (str): The unit of the input value ('m3', 'l', 'ml').
        target_unit (str): The desired output unit ('L', 'gal', etc.). Note: 
                          This function currently supports conversion to L or m³ from metric,
                          and to Liters/m³ from Imperial Gallons.

    Returns:
        tuple[float, str]: A tuple containing the converted value and its string representation.

    Raises:
        ValueError: If units are unsupported or volume is negative.
    """
    
    # Normalize input strings for internal processing if needed (handled by class logic)
    converter = VolumeConverter(source_unit.lower(), target_unit.lower())
    
    try:
        result_value, result_string = converter.convert(volume_value)
        
        # Special case handling for mL conversion via the specific method 
        # or ensuring general coverage. The generic convert handles L and M3 well.
        # For strict mL support in a unified flow without complex logic branching per unit type inside __init__:
        if source_unit == 'ml':
            ml_value = volume_value / 1000.0 # Convert to Liters first? No, input is ML value directly usually.
                                            # Let's assume input argument is the magnitude of that specific unit.
            
            # Recalculate based on logic: Input mL means we have X milliliters.
            # We need to convert X mL -> Target Unit.
            liters = volume_value / 1000.0
            
            if target_unit in ('l',):
                return (liters, 'L')
            elif target_unit == 'm3':
                m3_val = liters / 1000.0
                return ((volume_value / 1_000_000), 'm³') # Direct calc: mL to M3 is divide by 1e6
            
        if source_unit in ('l',):
            liters = volume_value
            if target_unit == 'm3':
                m3_val = liters / 1000.0
                return ((volume_value / 1000), 'm³') # L to M3 is divide by 1000
                
        elif source_unit in ('gal',):
            gal_to_liters_volume = volume_value * 4.54609
            
            if target_unit == 'l':
                return (gal_to_liters_volume, 'L')
            else: # m3
                m3_val = gal_to_liters_volume / 1000.0
                return ((volume_value * 4.54609) / 1000.0, 'm³')

        # Fallback for generic logic if strict type hints are followed and class is used correctly above:
        converter = VolumeConverter(source_unit.lower(), target_unit.lower())
        
    except ValueError as e:
        raise e from None

if __name__ == '__main__':
    """Sample execution block demonstrating functionality."""

    # Sample 1: Convert cubic meters to Liters
    m3_to_l_result, unit = convert_volume(2.5, 'm3', 'L')
    print(f"Converted {2.5} m³ to {unit}: {m3_to_l_result:.4f}")

    # Sample 2: Convert Liters to Cubic Meters
    l_to_m3_result, unit = convert_volume(1000, 'l', 'm3')
    print(f"Converted {1000} L to {unit}: {l_to_m3_result:.4f}")

    # Sample 3: Convert Milliliters (assuming input is magnitude in mL)
    ml_to_l_result, unit = convert_volume(5000, 'ml', 'L')
    print(f"Converted {5000} mL to {unit}: {ml_to_l_result:.4f}")

    # Sample 4: Convert Imperial Gallons to Liters (using the logic derived in class)
    gal_to_l_result, unit = convert_volume(10.0, 'gal', 'L')
    print(f"Converted {10.0} gallons to {unit}: {gal_to_l_result:.4f}")

    # Sample 5: Convert Imperial Gallons to Cubic Meters
    gal_to_m3_result, unit = convert_volume(2.0, 'gal', 'm3')