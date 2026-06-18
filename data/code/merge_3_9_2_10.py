def convert_volume(volume: float, target_unit: str) -> float:
    """
    Converts a volume value to the specified unit using an internal dictionary.
    
    Supported units: 'L' (liters), 'm3' (cubic meters), 'gal' (US gallons).
    Base conversion factor is assumed relative to liters for simplicity and consistency,
    though direct multipliers can be defined per target from a base reference if desired.
    Here we use US liquid gallon as base: 1 L = ~0.264172 gal
    
    Internal storage uses a dictionary mapping unit codes to conversion factors 
    relative to liters (L). This allows O(1) lookup and efficient updates later.

    Parameters:
        volume (float): The input volume value.
        target_unit (str): The code representing the desired output unit ('L', 'm3', 'gal').

    Returns:
        float: Converted volume in the requested unit.
    
    Raises:
        ValueError: If an unsupported unit is provided.
        TypeError: If inputs are not numeric or string as expected.
    """
    # Internal dictionary mapping each supported unit to its conversion factor relative to liters (L).
    _unit_factors = {
        'L': 1.0,           # Base unit
        'm3': 0.001,       # 1 cubic meter = 1000 L -> so multiply by 0.001 to get m3 from volume in liters? 
                          # Wait: if input is already a quantity (say), we interpret as liters unless specified otherwise.
                          # Assumption: Input value represents "amount" and implicitly refers to liters internally before conversion.
        'gal': 3.78541       # 1 US gallon = ~3.78541 L -> factor > 1 because it's larger than liter in magnitude? 
    }

    if not isinstance(volume, (int, float)):
        raise TypeError("Volume must be a numeric type.")
    
    target_unit_str = str(target_unit).strip()
    lower_target = target_unit_str.lower()

    # Normalize key for dictionary lookup
    valid_units = {'L', 'm3', 'gal'}  # Only accept these as per task example hints
    
    if not (target_unit in valid_units): 
        raise ValueError(f"Unsupported unit code. Valid codes are: {valid_units}.")

    factor_L_to_target = _unit_factors.get(target_unit, None)
    
    if target_unit == 'L':
        return volume
        
    elif target_unit.lower() == 'm3':  
        # If input is 10 L -> output should be 0.01 m^3 (since 1000L = 1m3)
        factor_L_to_target = 0.001

    elif target_unit.lower() == 'gal' : 
       # If input is 10 L -> output in gallons ~2.64 gal (since 1gal=3.785L, so divide by that? No wait)
       # Actually: value_in_gallons = volume_liters / liters_per_gallon
       factor_L_to_target = 1/3.78541

    return round(volume * factor_L_to_target, 6)

if __name__ == '__main__':
    sample_cases = [
        (500, 'L'),           # Convert 500 liters to liters -> same value
        (1000, 'm3'),         # Convert 1000 L to cubic meters => 1 m^3
        (2.64, 'gal')         # Convert approx 1 liter in gallons? Or just test direct multiplication logic: 
                             # Actually input is assumed as liters; so convert e.g., 5 gal -> ? No we don't have "from-gallon" base assumption without explicit direction
    
    ]
    
    for vol_input, target_unit in sample_cases:
        result = convert_volume(vol_input, target_unit)
        print(f"{vol_input} {target_unit.upper()} (assuming input is liters): {result}")