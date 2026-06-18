import math

def convert_distance(value: float, from_unit: str, to_unit: str) -> tuple[float, str]:
    """
    Converts a distance value between meters, kilometers, and miles with input validation.
    
    Args:
        value (float): The numerical value of the distance.
        from_unit (str): Source unit ('m', 'km', or 'mi').
        to_unit (str): Target unit ('m', 'km', or 'mi').
        
    Returns:
        tuple[float, str]: A tuple containing the converted float value and the target unit string.
        
    Raises:
        ValueError: If units are invalid, numeric input is non-numeric, conversion factor calculation overflows (extremely rare).
    
    Standardized base unit is meters (m). Conversion factors from meters:
    1 km = 1000 m
    1 mi ≈ 1609.344 m
    
    Note: Input validation ensures no interactive prompts or external dependencies are used.
    """

    # Define valid units for clarity and error handling
    VALID_UNITS = {'m': 'meter', 'km': 'kilometer', 'mi': 'mile'}
    
    def _normalize_unit(unit_str: str) -> str | None:
        """Normalizes the input unit string to a standard key."""
        return (unit_str.lower().strip(' ,') or '') if unit_str else ''

    # Validate units against allowed set and normalize strings for user feedback
    from_key = _normalize_unit(from_unit).lower()
    to_key = _normalize_unit(to_unit).lower()
    
    valid_from_keys: dict[str, str] | None = VALID_UNITS.get(from_key)

if __name__ == '__main__':
    pass
