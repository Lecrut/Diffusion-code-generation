def adjust_distance(distance: float, from_unit: str) -> tuple[float, dict]:
    """
    Adjusts a distance value to the opposite unit (km <-> miles).
    
    Args:
        distance (float): The numerical distance value.
        from_unit (str): The current unit ('miles' or 'km').
        
    Returns:
        tuple[float, dict]: A tuple containing the adjusted distance and 
                           a dictionary showing the conversion factor used.
                           
    Examples:
        adjust_distance(10, 'miles') -> (16.09344, {'factor': 1.60934})
        adjust_distance(50, 'km') -> (31.06856, {'factor': 0.621371})
    """
    
    # Define conversion factors to kilometers first for consistency
    factor_to_km = {
        "miles": 1.60934,      # miles * 1.60934 = km
        "km": 1.0               # identity
    }
    
    factor_from_other = {}
    
    if from_unit == 'miles':
        adjusted_distance = distance * factor_to_km['miles']
        # To get miles back, we divide by the forward factor or multiply by its reciprocal
        factor_back = 1.0 / factor_to_km["miles"]
        label_label_display_text: dict[str, str]

if __name__ == '__main__':
    pass
