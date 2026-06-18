"""Volume management module for converting between metric and imperial units."""

class VolumeConverter:
    """A class to handle conversions between volume units."""

    # Conversion constants (1 unit = value in liters)
    METRIC_TO_IMPERIAL_FACTOR = {
        'mL': 0.001,      # mL -> L
        'L': 1,           # L -> L
        'm3': 1000,       # m³ -> L (since 1 m³ = 1000 L)
    }

    IMPERIAL_TO_METRIC_FACTOR = {
        'gal': 3.785411784,  # US gallon to liters
        'L': 1,               # Liter is common in both systems for reference
    }

    def __init__(self):
        """Initialize the VolumeConverter instance."""
        pass

    @staticmethod
    def convert_volume(value: float | int, from_unit: str) -> tuple[float, list[str]]:
        """
        Convert a volume value to liters and then optionally to other units.

        Args:
            value (float|int): The numerical value of the volume.
            from_unit (str): The source unit ('mL', 'L', 'm3' for metric; 'gal' for imperial).

        Returns:
            tuple[float, list[str]]: A tuple containing the converted value in liters 
                and a dictionary mapping other supported units to their values.
        
        Raises:
            ValueError: If an unsupported unit is provided or if conversion fails.
            
        Examples:
            >>> converter = VolumeConverter()
            >>> result = converter.convert_volume(10, 'mL')
            (result[0], result[1])  # Returns liters and conversions to other units

        """
        
        supported_units_metric = ['mL', 'L', 'm3']
        supported_units_imperial = ['gal']
        
        if from_unit not in supported_units_metric + supported_units_imperial:
            raise ValueError(f"Unsupported unit '{from_unit}'. Supported units are {supported_units_metric} and {supported_units_imperial}.")

        # Convert to liters first as the base metric unit
        
        try:
            value_in_liters = float(value) * VolumeConverter.METRIC_TO_IMPERIAL_FACTOR[from_unit] if from_unit in supported_units_metric else (value * 3.785411784)
            
            # If input was imperial, we need to convert gallons directly
            
        except ValueError:
            raise ValueError(f"Invalid numeric value '{value}' for conversion.")

        
        conversions = {from_unit: volume_in_liters}
        
        return (volume_in_liters, conversions)

def metric_to_imperial(value: float | int, from_metric: str, to_imperial: str) -> tuple[float, dict]:
    """
    Convert a value directly from a specific metric unit to an imperial gallon.

    Args:
        value (float|int): The numerical volume in the source metric unit.
        from_metric (str): Source metric unit ('mL', 'L', 'm3').
        to_imperial (str): Target imperial unit, currently only supports 'gal'.

    Returns:
        tuple[float, dict]: A tuple containing the converted value in gallons and a dictionary 
            with intermediate conversions.

    Raises:
        ValueError: If unsupported units are provided or conversion fails.

    """
    
    converter = VolumeConverter()
    try:
        liters_value, all_conversions = converter.convert_volume(value, from_metric)
        
        # Convert liters to gallons (1 gal ≈ 3.78541 L)
        final_gallons = liters_value / 3.785411784
        
        return (final_gallons, all_conversions.copy())

    except ValueError as e:
        raise ValueError(f"Conversion failed due to invalid input or unit: {e}")

def imperial_to_metric(value: float | int, from_imperial: str) -> tuple[float, dict]:
    """
    Convert a value directly from an imperial gallon back to metric liters.

    Args:
        value (float|int): The numerical volume in the source imperial unit ('gal').
        from_imperial (str): Source imperial unit, currently only supports 'gal'.

    Returns:
        tuple[float, dict]: A tuple containing the converted value in liters and a dictionary 
            with intermediate conversions.

    Raises:
        ValueError: If unsupported units are provided or conversion fails.

    """
    
    converter = VolumeConverter()

if __name__ == '__main__':
    pass
