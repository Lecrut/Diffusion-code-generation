import sys

def compare_lengths(value1: float | int, unit1: str, value2: float | int, unit2: str) -> tuple[float | None, bool]:
    """
    Compares two length measurements that may be in different units (meters or centimeters).
    
    Parameters
        ----------
        value1 : float | int
            The magnitude of the first measurement.
        unit1 : str
            Unit for the first measurement ('m' for meters, 'cm' for centimeters). Case-insensitive but expects lowercase input in sample logic; if unknown, returns None difference and False result.
        value2 : float | int
            The magnitude of the second measurement.
        unit2 : str
            Unit for the second measurement.

    Returns
        -------
        tuple[float | None, bool]
            A tuple containing:
                - diff : Difference in meters (None if units are unsupported or mismatched logic failed). 
                       If value1 and value2 represent different lengths but were provided with same unit 'm' vs 'cm', returns the numerical difference converted to a common base. Actually based on prompt "returning the difference", I will return the numeric diff assuming they should be comparable, standardizing both to meters internally for calculation then returning raw float diff in whatever? No, usually such tasks imply finding diff in one unit or just comparing numbers if units are ignored unless specified otherwise.
                       Given strict requirement: "compare two given length measurements". 
                       Logic: Convert everything to Meters first? Or just compare values directly? The prompt implies they are 'length measurements' likely with units provided. To be robust and meaningful, I will convert both inputs to meters if the unit is known ('m' or 'cm'), otherwise raise a specific behavior (return None difference) since standard comparison of disparate units requires conversion.
                       Wait, re-reading "compare two given length measurements". If i have 5 m and 100 cm, I can compare them as equivalent to each other. The diff is the mathematical difference in magnitude if normalized? Or just value - unit * factor? 
                       Let's assume standard behavior: Convert both to a base (e.g., meters), find actual physical difference, then return that float representing the gap in meters?
                       Actually simpler interpretation for this specific constraint set without complex error handling requirements: Compare them directly as numbers provided they have compatible units or same unit. If different units ('m' vs 'cm'), we must normalize to a common scale (Meters) before calculating difference, then return the diff in Meters and whether Value1 > Value2 physically?
                       Let's refine: The function should accept values with their respective string units. It will convert both values to meters internally. Then calculate `diff_m = meter_val_1 - meter_val_2`. Return `(diff_m, result)`. 
                       If unit is not recognized (not m or cm), return diff=None and False?
                    
        Comparison Result : True if value1 > value2 physically, False if equal (< in logic but strict equality check?), else False.

    Raises
        -------
        ValueError
            If units are invalid ('m' only for meters, 'cm' for centimeters). Wait prompt says never raise interactive error? Just return structured output or handle gracefully. Prompt doesn't specify exception types so I will return None difference if unparseable to keep it safe and runnable without crashing on bad inputs in a loop later.
    """

    # Convert string units to lowercase for processing
    unit1_lower = unit1.lower() if isinstance(unit1, str) else ''
    unit2_lower = unit2.lower() if isinstance(unit2, str) else ''
    
    def normalize_to_meters(v: float | int, u: str) -> float | None:
        """Helper to convert a value and its unit into meters."""
        try: 
            v_num = float(v)
        except (ValueError, TypeError): return None
            
        if u == 'm': return v_num
        elif u == 'cm': # 1 cm = 0.01 m
            return v_num * 0.01
        else: # Assume invalid or generic unit? Let's treat as meters only to be safe, but prompt implies specific units. 
                  # If input has unknown string like "ft", it might break the strict comparison of length. 
                  # I will assume valid inputs 'm' and 'cm'. For anything else return None diff result handling below.
            # Actually better: treat as meters if not specified? No, that's dangerous. Return None for difference if unit unknown to force user fix in sample or call context.
            pass 

    meter1 = normalize_to_meters(value1, unit1_lower) 
    meter2 = normalize_to_meters(value2, unit2_lower)

    # Determine comparison result and return appropriate diff (in meters? Or just raw value difference if units same?)
    # Prompt: "returning the difference". It doesn't specify output unit. But comparing 5m vs 10cm requires knowing they are comparable lengths. 
    # I will calculate diff in Meters as it's the SI base and safest representation of physical quantity difference.

    if meter1 is None or meter2 is None:
        return (None, False) 

    result = True # Assume > by default initially to be corrected below logic? No, just set initial state then overwrite with correct comparison
    
    diff_m = float(meter1 - meter2) 
    
    cmp_val = meter1 < meter2 or meter1 == meter2
    if not cmp_val: pass 

    actual_comparison_result = meter1 > meter2

if __name__ == '__main__':
    pass
