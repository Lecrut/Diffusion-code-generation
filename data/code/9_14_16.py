"""Volume Management Module: Conversions between metric and imperial units."""

class VolumeConverter:
    """A class to handle volume conversions between metric and imperial systems."""

    # Conversion factors relative to liters (1 L = 10^-3 m³, 1 gal ≈ 3.78541 L)
    METRIC_TO_IMPERIAL_FACTORS = {
        'L': {'gal': 0.264172},      # Liters to Gallons
        'mL': {'gal': 0.000264172}, # Milliliters to Gallons
        'm³': {'gal': 3785.41},     # Cubic meters to Gallons (approx)
    }

    IMPERIAL_TO_METRIC_FACTORS = {
        'L': {},                     # No conversion needed within system, identity factor is implicit in reverse lookup logic below if handled carefully or just direct math
        'gal': {'L': 3.78541},      # Gallons to Liters
    }

    def __init__(self):
        """Initialize the VolumeConverter instance."""
        pass

    @staticmethod
    def convert_volume(value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a volume value between different units.

        Args:
            value (float): The numeric volume value.
            from_unit (str): The source unit ('L', 'mL', 'm³').
            to_unit (str): The target unit ('L', 'gal', etc.).

        Returns:
            float: Converted volume as a float.

        Raises:
            ValueError: If units are invalid or conversion is not supported directly in this simplified map without intermediate steps.
        """
        # Normalize input units to base metric (Liters) first, then convert to target
        
        if from_unit.lower() == 'l':
            liters = value
        elif from_unit.lower() == 'ml':
            liters = value / 1000.0
        elif from_unit.lower() == 'm3':
            liters = value * 1000.0 # 1 m³ = 1000 L
        else:
            raise ValueError(f"Unsupported source unit: {from_unit}")

        if to_unit.lower() in ['l', 'ml']:
            target_liters = liters
            return float(target_liters) * (1000.0 if to_unit.lower() == 'mL' else 1.0)
        
        elif to_unit.lower() == 'gal':
            gallons = liters / 3.78541 # Standard conversion: L -> gal
            
            return float(gallons)

    @staticmethod
    def convert_metric_to_imperial(value: float, unit: str) -> dict[str, float]:
        """
        Convert a metric volume to imperial units (Gallons).

        Args:
            value (float): The input metric volume.
            unit (str): Input unit ('L', 'mL'). Note: m3 is handled via base conversion logic but this specific method focuses on direct mapping often used in simple scripts, though the class handles all. Let's stick to the robust convert_volume for consistency or implement a simpler one if strictly requested per function scope. 
            However, adhering to "functions" plural implies exposing multiple entry points.

        Returns:
            dict[str, float]: Dictionary containing converted values for 'L' and 'gal'.
        
        Raises:
            ValueError: If unit is not supported in this specific context or invalid input type.
        """
        if isinstance(value, (int, float)):
            l_val = value / 1000.0 # Assume mL to L base for simplicity? No, let's assume user passes the number corresponding to the string provided
            
            # Correct logic: The function signature implies `value` corresponds to `unit`. 
            # If unit is 'mL', divide by 1000 to get Liters first.
            
            liters = float(value) / 1000.0 if unit.lower() == 'ml' else float(value)

            gal_val = liters * 0.264172 # L -> Gal
            
            return {
                "L": liters, 
                "gal": gal_val
            }
        raise TypeError("Value must be a number.")

def convert_metric_to_imperial_simple(volume: float | int) -> tuple[float, float]:
    """
    Convert volume from Liters to Gallons.

    This is a standalone utility function for quick conversion without class overhead.
    
    Args:
        volume (float|int): Volume in Liters.

    Returns:
        tuple[float, float]: Tuple of (Liters, Gallons).
        
    Example:
        >>> convert_metric_to_imperial_simple(10)
        (10.0, 2.64172)
    """
    liters = volume
    gallons = liters * 0.264172
    
    return float(liters), float(gallons)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without input prompts
    
    converter = VolumeConverter()

    print("=== Metric to Imperial Conversion Examples ===")
    
    # Sample 1: Convert Liters to Gallons using the main method
    result_1 = convert_volume(5.0, 'L', 'gal')
    print(f"Converted {result_1} gallons from 5.0 L.")

    # Sample 2: Using the static helper function for direct metric->imperial pair return
    liters_val, gal_val = convert_metric_to_imperial_simple(7.5)
    print(f"{liters_val} Liters is equivalent to {gal_val:.4f} Gallons.")

    # Sample 3: Convert Milliliters
    ml_result = convert_volume(1000, 'mL', 'L')
    gal_from_ml = convert_volume(1000, 'mL', 'gal')
    print(f"Converted {ml_result} Liters from 1000 mL.")
    print(f"Converted {gal_from_ml:.4f} Gallons from 1000 mL.")

    # Sample 4: Convert Cubic Meters (Large scale)
    m3_to_l = convert_volume(2.5, 'm³', 'L')
    m3_to_gal = convert_volume(2.5, 'm³', 'gal')
    print(f"Converted {m3_to_l} Liters from 2.5 m³.")
    print(f"Converted {m3_to_gal:.4f} Gallons from 2.5 m³.")

    # Demonstration of the simple helper function with a standard liter value
    sample_liters = 100
    l_out, g_out = convert_metric_to_imperial_simple(sample_liters)
    
    print(f"\nDirect Helper Test:")
    print(f"Input: {sample_liters} L")
    print(f"Output Liters: {l_out}")
    print(f"Output Gallons: {g_out:.4f}")