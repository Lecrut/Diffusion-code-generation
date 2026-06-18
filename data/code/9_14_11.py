"""Volume management module for converting between metric and imperial units."""

class VolumeConverter:
    """A class to handle conversions between volume units."""

    # Conversion factors relative to cubic meters (m³)
    METRIC_TO_CUBIC_METERS = {
        'L': 0.001,           # 1 Liter = 0.001 m³
        'mL': 0.000001,       # 1 mL = 1e-6 m³
    }

    IMPERIAL_TO_CUBIC_METERS = {
        'gal': 0.003785411784,  # 1 US gallon ≈ 0.003785... m³ (exact: 231 in³)
    }

    def __init__(self):
        """Initialize the VolumeConverter with standard conversion factors."""
        pass

    @staticmethod
    def convert_metric_to_imperial(value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a volume value from metric units (L or mL) to imperial units (gal).

        Args:
            value (float): The numeric volume value.
            from_unit (str): Source unit ('L' or 'mL').
            to_unit (str): Target unit, currently only supports 'gal'.

        Returns:
            float: Converted volume in the target imperial unit.

        Raises:
            ValueError: If unsupported units are provided.
        """
        if from_unit not in VolumeConverter.METRIC_TO_CUBIC_METERS:
            raise ValueError(f"Unsupported metric source unit: {from_unit}")
        
        # Convert to cubic meters first, then to gallons
        value_in_m3 = volume_to_cubic_meters(value, from_unit)
        return convert_cubic_meter_to_gal(volume_in_m3)

    @staticmethod
    def convert_imperial_to_metric(value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a volume value from imperial units (gal) to metric units (L or mL).

        Args:
            value (float): The numeric volume value.
            from_unit (str): Source unit ('gal').
            to_unit (str): Target unit ('L' or 'mL').

        Returns:
            float: Converted volume in the target metric unit.

        Raises:
            ValueError: If unsupported units are provided.
        """
        if from_unit not in VolumeConverter.IMPERIAL_TO_CUBIC_METERS:
            raise ValueError(f"Unsupported imperial source unit: {from_unit}")
        
        # Convert to cubic meters first, then to target metric unit
        value_in_m3 = convert_gal_to_cubic_meter(value)
        return cubic_meters_to_volume(value_in_m3, to_unit)

    @staticmethod
    def convert_metric_to_metric(value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a volume value directly between metric units (L or mL).

        Args:
            value (float): The numeric volume value.
            from_unit (str): Source unit ('L' or 'mL').
            to_unit (str): Target unit ('L' or 'mL').

        Returns:
            float: Converted volume in the target metric unit.
        """
        if from_unit not in VolumeConverter.METRIC_TO_CUBIC_METERS:
            raise ValueError(f"Unsupported metric source unit: {from_unit}")
        
        # Convert to cubic meters, then back to target metric unit
        value_in_m3 = volume_to_cubic_meters(value, from_unit)
        return cubic_meters_to_volume(value_in_m3, to_unit)

def convert_gal_to_cubic_meter(gallons: float) -> float:
    """Convert US gallons to cubic meters."""
    return gallons * VolumeConverter.IMPERIAL_TO_CUBIC_METERS['gal']

def volume_to_cubic_meters(volume_value: float, unit: str) -> float:
    """Convert any supported metric or imperial unit to cubic meters."""
    if unit in VolumeConverter.METRIC_TO_CUBIC_METERS:
        return volume_value * VolumeConverter.METRIC_TO_CUBIC_METERS[unit]
    
    # Handle US gallons via the dedicated function for clarity, though could be merged here.
    raise ValueError(f"Unit {unit} not directly supported by this helper; use convert_imperial_to_metric or convert_gal_to_cubic_meter.")

def cubic_meters_to_volume(cubic_meters: float, unit: str) -> float:
    """Convert cubic meters to any supported metric or imperial unit."""
    if unit == 'L':
        return cubic_meters * 1000.0
    
    elif unit == 'mL':
        return cubic_meters * 1_000_000.0
    
    elif unit == 'gal':
        # Inverse of IMPERIAL_TO_CUBIC_METERS factor (approx) or exact calculation: m3 / 231 in³ -> gal? 
        # Actually, gallons = cubic_meters * (1/Volume_of_1_gal_in_cubic_meters)
        return cubic_meters / VolumeConverter.IMPERIAL_TO_CUBIC_METERS['gal']

    raise ValueError(f"Unsupported target unit: {unit}")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    converter = VolumeConverter()
    
    print("=== Metric to Imperial Conversion ===")
    try:
        liters_to_gal = convert_metric_to_imperial(10, 'L', 'gal')
        ml_to_gal = convert_metric_to_imperial(5000, 'mL', 'gal')
        print(f"10 L -> {liters_to_gal:.6f} gal")
        print(f"5000 mL -> {ml_to_gal:.6f} gal")
    except ValueError as e:
        print(f"Error in metric to imperial conversion: {e}")

    print("\n=== Imperial to Metric Conversion ===")
    try:
        gallons_to_l = convert_imperial_to_metric(5, 'gal', 'L')
        gallons_to_ml = convert_imperial_to_metric(0.125, 'gal', 'mL')
        print(f"5 gal -> {gallons_to_l:.6f} L")
        print(f"0.125 gal -> {gallons_to_ml:.6f} mL")
    except ValueError as e:
        print(f"Error in imperial to metric conversion: {e}")

    print("\n=== Metric to Metric Conversion ===")
    try:
        l_to_l = convert_metric_to_metric(2, 'L', 'mL')  # Should be equivalent but different scale representation logic check? No, direct conversion.
        ml_to_ml = convert_metric_to_metric(1000, 'mL', 'L')
        print(f"2 L -> {l_to_l:.6f} mL")
        print(f"1000 mL -> {ml_to_ml:.6f} L")
    except ValueError as e:
        print(f"Error in metric to metric conversion: {e}")

    # Additional direct function tests for robustness demonstration
    try:
        gal_direct = convert_gal_to_cubic_meter(1)
        l_from_m3 = cubic_meters_to_volume(gal_direct, 'L')
        ml_from_m3 = cubic_meters_to_volume(gal_direct, 'mL')
        print(f"\nDirect conversion test (1 gal):")
        print(f"  Cubic meters: {gal_direct:.6f} m³")
        print(f"  Equivalent in L: {l_from_m3:.6f}")
        print(f"  Equivalent in mL: {ml_from_m3:.6f}")
    except ValueError as e:
        print(f"\nError in direct conversion test: {e}")