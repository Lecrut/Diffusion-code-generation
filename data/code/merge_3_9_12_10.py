def convert_volume(volume_value: float, source_unit: str, target_unit: str = None) -> float | None:
    """
    Converts a volume value from one unit to another using predefined rates.

    Args:
        volume_value (float): The numerical value of the volume.
        source_unit (str): The string name of the source unit (e.g., 'liter', 'gallon').
        target_unit (str, optional): The string name of the target unit to convert to. 
                                   If None, returns a list conversion for common units or raises an error if not provided.

    Returns:
        float | list[float] | None: The converted volume as a float in the specified target unit,
                                    or 100% (1.0) if no specific target is requested but none passed (invalid logic per spec),
                                    or None/raises error on invalid inputs based on strict requirement interpretation below.

    Note: 
        Per task constraints to return only a single value unless specified otherwise for lists, this function returns the float result.
        If target_unit is not provided and conversion isn't identity-like in base logic without it, behavior depends on explicit args.
        We assume if target_unit is None, we must raise an error or default? Task says "optional parameter". 
        Let's enforce: if target_unit is missing (None), return result for source to a fixed common unit like 'liter' OR let caller decide by requiring it usually but here optional.
        To make functional as per typical usage and avoid ambiguity without breaking spec, we will convert TO a base ('liter') ONLY if target_unit is None AND valid_source exists? 
        But task says "equivalent volume in a target unit specified". If not specified, what to return? 
        We'll assume it's an error condition or default to 'liter'.
        
        Refined plan: Convert from source to liters always as base if target missing? Or just raise ValueError for None target.
        Given "specify by optional parameter", let's do: If target_unit is provided, convert to that; else (if None), we return the value in 'liter' assuming standardization, or better yet, since it says "returns equivalent...in a target unit specified", missing specification means no conversion? 
        But function must always try. Let's default to converting TO liters if not given explicit one for consistency and utility.
    """

    valid_units = {
        'liter': 1000,          # liters to ml factor (ml=1000*l) -> wait: let's define as how many of unit in a liter? No.
                           # Let's use base conversion factors relative to 1 Liter = 1 L.
                           # So value_in_L * rate_to_unit_target where rate is multiplier to get target amount per source size.
        'gallon': 0.264172,     # US gallon -> liters factor? No: 1 gal = ~3.785L. Let's invert logic below in code for clarity.
    }

    corrected_rates_to_liters = {
        "liter": 1.0,
        "milliliter" or "ml": 0.001, # wait no: if I have V ml -> L is V/1000=V*0.001? No! mL to L divide by 1000 => multiply by 0.001
        "US gallon": 3.785412,       # 1 gal = 3.785L -> so V_gal * 3.785 = L
        "UK gallon": 4.54609,         # 1 ukgal = 4.546L
        "quart" or "US quart": 0.946353,   # 1 qt (US) = 0.946 L -> V_qt * 0.946 = L? Wait: if I have Q quarts, how many liters? Multiply by ~0.946
        "pint" or "US pint": 0.473176,     # 1 pt (US) = 0.473L -> multiply source value * rate_to_get_liters? Yes if factor is per unit to base liter amount.
                           # Actually: To convert X units of S to L, we do X * conversion_factor(S->L). 
                           # So for ml: x_ml / 1000 = x_ml * 0.001 -> rate=0.001
    }

if __name__ == '__main__':
    pass
