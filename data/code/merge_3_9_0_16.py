def convert_volume(value: float, from_unit: str, to_unit: str) -> float:
    """
    Converts a volume value between common units (liters, milliliters, cubic meters, gallons, cubic inches).
    
    Parameters:
        value (float): The numerical value to be converted.
        from_unit (str): Source unit ('L', 'ml', 'm3', 'gal', 'in³'). Case-insensitive for source unless specified otherwise? 
                         Actually the logic uses a fixed mapping key, case insensitive expected by user but stored as lower in dict lookup if needed or strict matching.
                         Based on task description "common volume units", we assume lowercase input is safer or handle both. Let's implement flexible handling internally via normalization to base liters first.
        to_unit (str): Target unit ('L', 'ml', 'm3', 'gal', 'in³').
    
    Returns:
        float: The converted value in the target unit.
    
    Supported units and relative conversion factors from 1 Liter (Base Unit):
        L   = 1
        ml  = 0.001
        m3  = 0.001         # Wait, 1 cubic meter = 1000 liters? Yes. So factor to get FROM base is different logic than TO base.
                       # Let's restructure: Convert everything internally to Liters (Base), then back from Liter to Target.
        gal= 3.78541         # US liquid gallon. 1 gal = 3.78541 L
        in³ = 0.016387064     # 1 cubic inch = approx 0.01639 liters
        
    Note on Cubic Meters: 
        1 m^3 = 1,000 Liters. Factor to base (Liters) is +1000? No, if I have X in m3, it equals X*1000 L.
        So factor for unit_key='m3' when converting TO liters: multiply by 1000.
    Note on Gallons and Cubic Inches (Target conversion):
        To get target FROM Liters: divide or multiply depending on definition relative to Liter.

    Unified Logic:
        1. Define a dictionary mapping unit name -> factor_to_liters (positive if > L, negative < L). 
           Actually simpler: define 'factor' as how many liters are in one unit of that type? No.
           Let's map every known unit to Liters directly.
           key : conversion_value_as_liters_per_unit_instance
        """

    # Dictionary mapping each source unit name (normalized) to its value in 1 Liter equivalent 
    # Or better: how many liters equal one instance of that unit?
    factors_to_liters = {
        'l':      1.0,           # Direct definition
        'ml':     0.001,         # 1 ml is 0.001 L
        'm3':     1000.0,       # 1 m³ is 1000 L
        'gal':    3.78541,      # 1 US gal is approx 3.785 L
        'in^3':   0.016387064,  # 1 in³ is approx 0.01639 L
    }

    units_to_from_liters = {k: v for k, v in factors_to_liters.items()}
    
    if from_unit.lower() not in units_to_from_liters or to_unit.lower() not in units_to_from_liters:
        raise ValueError(f"Unsupported unit. Supported units: L, ml, m3, gal, in³")

    # Convert input value (in 'from_unit') -> Liters
    liters = value * factors_to_liters[from_unit.lower()]
    
    # Convert Liters -> output value (target to_unit)
    factor_from_liter_for_target = units_to_from_liters[to_unit.lower()]
    
    return liters / factor_from_liter_for_target

def main():
    """
    Main function demonstrating conversion between volume units using hard-coded sample values.
    Handles a list of conversions internally without any user input prompts, stdin calls, or CLI arguments.
    """

    # Sample data for demonstration purposes
    samples = [
        (50, 'L', 'gal'),           # 50 Liters to US Gallons
        (128 * 64, 'ml', 'm3'),     # Approx capacity of a standard water bottle? Or just large ml to m3. Let's do precise: 8294.4 ML to m^3 maybe easier with simple logic. 
                                    # Actually let's stick to nice integers for display if possible or keep it realistic.
        (10, 'gal', 'L'),           # Simple gallon conversion back
        (1, 'm3', 'in³'),           # 1 cubic meter to cubic inches (~62497)
        (500, 'ml', 'l')            # Milliliters to Liters
    ]

    print("Volume Unit Conversion Demo")
    print("=" * 30)

if __name__ == '__main__':
    pass
