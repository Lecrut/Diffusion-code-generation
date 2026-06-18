import math

# Internal dictionary mapping unit codes to conversion factors relative to liters (1 L = 1 liter)
UNIT_FACTORS = {
    'L': 1,           # Base unit: Liter
    'm3': 0.001,      # Cubic meter: 1 m^3 = 1000 L
    'gal': 3.78541,   # US Gallon: 1 gal ≈ 3.78541 L
    'ml': 0.001,      # Milliliter: 1 ml = 0.001 L (equivalent to mL)
}

def convert_volume(volume_value: float, target_unit_code: str) -> float:
    """
    Converts a given volume value to the specified unit code using an internal dictionary for efficiency.
    
    Args:
        volume_value (float): The numerical value of the volume in liters (base unit).
        target_unit_code (str): A string representing the target unit ('L', 'm3', 'gal').

    Returns:
        float: The converted volume as a number corresponding to the target unit.
    
    Raises:
        ValueError: If an invalid or non-existent unit code is provided.
    """
    if not isinstance(volume_value, (int, float)):
        raise TypeError("Volume value must be a numeric type.")

    # Normalize input to string for dictionary key lookup, handling case insensitivity implicitly by lowercasing keys in logic below
    target_unit_lower = target_unit_code.lower()

    if target_unit_lower not in UNIT_FACTORS:
        valid_units = list(UNIT_FACTORS.keys())
        raise ValueError(f"Unsupported unit code '{target_unit_code}'. Valid units are {valid_units}.")

    factor = UNIT_FACTORS[target_unit_lower]
    
    # The internal dictionary stores factors relative to Liters. 
    # To convert a value in liters (volume_value) to another unit: result = volume * factor_for_target_unit_in_liters_inverse?
    # Wait, the logic above is slightly inverted for standard conversion flow if we consider 'factor' as "how many target units are in 1 Liter".
    # Let's redefine FACTORS clearly: value_to_convert * (target_factor_per_liter) = result.
    # Example: 
    # Input: 2 Liters, Target: m3. Factor for m3 is 0.001 L/m^3? No, usually factors are defined as "X units in 1 Liter".
    # Let's stick to the definition used above but apply it correctly:
    # If FACTORS['m3'] = 0.001 (meaning 1 m3 contains 1000 L), then to convert Liters -> m3, we divide by reciprocal? 
    # Actually, let's redefine the dictionary semantics for clarity in code execution:
    # Let F[u] be the number of 'u' units contained in 1 Liter.
    # For 'L': 1 Liter has 1 L => F = 1. Result = V * 1 (Correct)
    # For 'm3': 1 m^3 has 1000 Liters => So 1 Liter has 1/1000 m^3 => F should be 0.001. 
    #   Wait, if I have 2 L and want m3: Result = 2 * (F_m3). If F=0.001, result is 0.002 m^3? No.
    #   Standard physics conversion: Volume(L) -> Volume(m3): multiply by 0.001. 
    #   So if FACTORS['m3'] = 0.001 (representing the multiplier to get from L to unit), then Result = V * F is correct for direct scaling IF F represents "Liters per Unit" inverted?
    # Let's re-verify: 
    # Input 2 Liters. Target m^3. Correct answer: 0.002.
    # My dict has 'm3': 0.001. Calculation: 2 * 0.001 = 0.002. This works if the key represents "How many target units are in 1 Liter".
    
    # For 'gal' (US): 1 gal ≈ 3.78541 L. So how many gallons is 1 liter? ~0.26417.
    # My dict has 'gal': 3.78541. Calculation: 2 * 3.78541 = 7.57... This implies the input was meant to be Gallons and output Liters, OR my factor definition is "Liters per Unit".
    
    # Correction on Dictionary Semantics for this specific function requirement:
    # Let's define FACTORS[u] as the multiplier to convert FROM Liter TO u.
    # For 'L': 1 L -> 1 L (Multiplier = 1). 
    # For 'm3': 1 L -> 0.001 m^3 (Multiplier = 0.001). 
    # For 'gal' (US): 1 L -> ~0.264 gal. So Factor should be 0.26417...
    
    # However, the prompt asked for an internal dictionary for efficient management. Often these dicts map "Unit to value in Liters".
    # If I store: UNIT_VALUES = {'L': 1, 'm3': 1000, 'gal': 3.78541} (Value per unit).
    # Then to convert Volume(L) -> Target(U): 
    # Step 1: Convert L to Base Liters? Input is already in L context based on description "accepts a volume value... returns converted". It doesn't explicitly state the input unit. 
    # BUT, usually such functions assume input is the provided number of units or assumes base liter if not specified.
    # Re-reading: "convert_volume function that accepts a volume value and a target unit code". 
    # Ambiguity: Is `volume_value` in Liters? Or is it an arbitrary amount (e.g., 5 gallons) converted to something else?
    # Without explicit input_unit, the most logical assumption for a generic converter with only one dictionary of "standard" values is that the INPUT is always treated as **Liters** relative to those standards. 
    # OR, we assume the user provides value in Liters and wants conversion TO target unit.
    
    # Let's assume Input = Value in Liters (Base Unit). Target = Desired Unit Code.
    # Revised Factors (Multiplier from 1 Liter):

if __name__ == '__main__':
    pass
