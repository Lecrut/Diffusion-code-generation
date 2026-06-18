import argparse

def get_unit_list():
    """Returns a list of supported units."""
    return ['m', 'km', 'cm', 'mm']

def convert_volume(value, start_unit, target_unit):
    """Converts volume between meters and kilometers using base unit conversion.
    
    Assumptions: 
    - Input value is in the starting unit (e.g., if input is 500 m).
    - Conversion logic assumes standard SI prefixes for length/volume representation here
      as a simplified model since 'volume' units like liters aren't strictly defined by just prefix.
      We treat this as linear distance scaled by volume factor of 1m^3 = 1L approximation 
      or simply convert the magnitude based on metric prefixes if interpreted as pure number scaling.
      
    For robustness in CLI context without external libraries, we'll implement a direct conversion:
    - Base unit is 'm' (meter).
    - If start_unit == target_unit, return original value.
    - Convert to base unit then to target unit using standard metric multipliers.

    Note: This treats the input as if it were in cubic meters scaled by prefix for simplicity 
    given no explicit volume definition provided beyond "unit". A more complex implementation would require
    specific definitions (e.g., 1 km = 10^9 m³). Here we assume linear scaling of magnitude.

    Args:
        value (float): The numeric value to convert.
        start_unit (str): Starting unit ('m', 'km', 'cm', 'mm').
        target_unit (str): Target unit ('m', 'km', 'cm', 'mm').

    Returns:
        float: Converted volume in the target unit.
    """
    
    # Define conversion factors to base unit 'm'
    # Assuming input value is already scaled correctly for its prefix relative to m^3 or similar logic? 
    # To keep it robust and simple without external data, we'll assume the user provides a number that represents
    # the quantity in some consistent scale where:
    # 1 km = 1000 m (linear) -> but volume? Let's reinterpret as linear for safety or use standard metric scaling.
    
    # Re-evaluating: Since true volume conversion requires knowing base unit size, and we don't have that info,
    # we will assume the input is a magnitude in cubic meters scaled by prefix factor implicitly included in value? 
    # Or better yet, treat this as converting the numerical representation assuming 1 unit = X m^3.
    
    # Simplest robust approach given constraints: Treat units as linear prefixes applied to base volume (m³).
    # So if input is "500 km", it means 500 * (km factor) m³? No, that doesn't make sense physically.
    
    # Given the ambiguity and task constraint ("robust"), we will implement a conversion based on 
    # standard metric prefixes assuming the value represents cubic meters scaled by prefix:
    # e.g., if start_unit is 'km', multiply by 10^9 (since km³ = (1000m)³ = 1e9 m³).
    
    factors_to_m3 = {
        'm': 1,
        'km': 1_000_000_000, # 10^9
        'cm': 1_000_000_000_000_000, # (0.01m)^3 = 1e-6 m³ -> wait, cm is smaller so multiply by huge? No.
    }

    # Correction: 
    # If value is given as "500 km", does it mean 500 cubic kilometers or just the number scaled?
    # Without explicit definition, let's assume standard metric volume conversion where:
    # Base unit = m³ (cubic meter).
    # Conversion factor to get from start_unit to base_m3:
    # 'm' -> 1 * val is in m^3.
    # 'km' -> val is in km^3, so multiply by 10^(9) because (10^3)^3 = 10^9.
    # 'cm' -> val is in cm^3, divide by 10^6? Or if input value already accounts for prefix... 
    # Let's assume the user passes a number that represents the quantity in the unit provided.
    
    def get_multiplier(unit):
        """Gets multiplier to convert X units of 'unit' to cubic meters."""
        base = {'m': 1, 'km': 1e9, 'cm': 1e-6, 'mm': 1e-9} # Assuming input value is in that unit's volume
        return base[unit]

    start_mult = get_multiplier(start_unit)
    target_mult = get_multiplier(target_unit)

    # Convert to cubic meters then to target
    m3_value = value * start_mult
    
    final_result = m3_value / target_mult
    
    return final_result

def main():
    """Main entry point for the CLI application."""
    
    parser = argparse.ArgumentParser(
        description="Convert volume units between metric prefixes."
    )
    
    # Non-required arguments as per task constraints (no required args)
    group = parser.add_argument_group(title='Conversion Parameters')
    
    group.add_argument(
        '-v', '--value', 
        type=float, 
        default=500.0,
        help="The volume value to convert."
    )
    
    group.add_argument(
        '-s', '--start-unit', 
        dest='starting_unit',
        choices=['m', 'km', 'cm', 'mm'],
        default='m',
        help="Starting unit (e.g., m, km)."
    )
    
    group.add_argument(
        '-t', '--target-unit', 
        dest='ending_unit',
        choices=['m', 'km', 'cm', 'mm'],
        required=False, # Not strictly required but good practice; default to same if not provided? Task says no input prompts.
        help="Target unit (e.g., m, km)."
    )

    args = parser.parse_args()
    
    start_unit = args.starting_unit.lower()
    target_unit = args.target_unit.lower() if args.target_unit else None
    
    # If no target provided in CLI but we need to run sample without input, default logic applies.
    # However, task says "hard-coded sample values" in the block below which will override or be used directly? 
    # Actually, argparse handles command line; if none passed, it uses defaults.
    
    result = convert_volume(args.value, start_unit, target_unit)

    print(f"{args.value} {start_unit.upper()} is equal to {result:.2f} {target_unit.upper() if target_unit else 'm'}")

if __name__ == '__main__':
    # Hard-coded sample values as per requirement. 
    # Since argparse defaults are set above, we can simulate a specific run by passing args via sys.argv? 
    # But task says "Never call input(), sys.stdin". We cannot modify sys.argv easily without import or hack.
    # Instead, let's rely on the defaults and override in logic if needed OR just trust the default values provided in code.
    
    # To strictly satisfy "hard-coded sample values" that run without user input:
    # The argparse setup already has defaults (value=500, start='m', target=None). 
    # If target is None, our conversion function might fail or need handling? 
    # Let's ensure the default logic works. In convert_volume, if target_unit is None -> error in division by zero?
    
    # Fix: Ensure sample run has a valid target unit hardcoded via argparse defaults modification OR post-processing.
    # Better approach: Override args inside main before calling convert to simulate specific input without CLI flags.

    import sys
    
    # Simulate command line arguments for the sample case directly in memory if needed, 
    # but since we can't call input(), let's just ensure our defaults are sufficient or adjust logic.
    
    # Let's restructure slightly: The task says "Include an if __name__ == '__main__' block with hard-coded sample values."
    # This could mean setting sys.argv manually? No, that might be considered external manipulation. 
    # Instead, let's just ensure the defaults in argparse are set to a valid scenario or handle None target gracefully.

    # Revised plan: Set default for target_unit in main() if not provided by CLI (which is always true here since no args passed).
    
    sample_value = 500.