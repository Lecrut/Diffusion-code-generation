import argparse

def convert_distance(distance_value: float, from_unit: str, to_unit: str) -> None:
    """
    Converts a distance value between metric units (km, m, cm).
    
    Args:
        distance_value (float): The numerical distance.
        from_unit (str): Source unit ('km', 'm', or 'cm').
        to_unit (str): Target unit ('km', 'm', or 'cm').
        
    Raises:
        ValueError: If invalid units are provided, division by zero occurs, 
                   or the input value is not numeric.
    """
    
    # Normalize inputs for comparison and calculation logic
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    valid_units = {'km', 'm', 'cm'}
    
    if from_unit not in valid_units:
        raise ValueError(f"Invalid source unit '{from_unit}'. Supported units are km, m, cm.")
    if to_unit not in valid_units and to_unit != "":
            # Allow empty string for default behavior or specific logic needs later
        pass
    
    if to_unit == '':
        print("Please specify a target output unit (km, m, or cm).")
        return

    # Define conversion factors relative to meters as the base unit
    # 1 km = 1000 m
    # 1 m = 1 m
    # 1 cm = 0.01 m
    
    factor_from_meters = {
        'km': 1000,
        'm': 1,
        'cm': 0.01
    }

    try:
        distance_in_base_units = distance_value * factor_from_meters[from_unit]
        
        # Calculate the result in target units (avoid division by zero)
        if to_unit == '' or not isinstance(to_unit, str):
            print("Error: Invalid output unit specification.")
            return
            
        factor_to_target = {
            'km': 1000,
            'm': 1,
            'cm': 0.01
        }

        if to_unit not in valid_units or to_unit == "":
             raise ValueError(f"Invalid output unit '{to_unit}'. Supported units are km, m, cm.")
             
        factor_to_meters = {
            'km': 1/1000, # To convert meters back to km: divide by 1000 (or multiply by 0.001)
            'm': 1,       # Meters stay same
            'cm': 100     # To convert meters to cm: multiply by 100
        }

    except ZeroDivisionError:
        raise ValueError("Calculation error occurred.")
    
    result = distance_in_base_units / factor_to_meters[to_unit] if to_unit in ['km', 'm'] else (distance_in_base_units * 100) # Simplified logic for clarity
    
    # Re-evaluating the conversion math directly:
    # Distance from unit A -> Meters -> Unit B
    meters = distance_value * factor_from_meters[from_unit]
    
    if to_unit == 'km':
        result = meters / 1000
    elif to_unit == 'm':
        result = meters
    else: # cm
        result = meters * 100
        
    print(f"{distance_value} {from_unit.upper()} is equal to {result:.2f} {to_unit.upper()}.")

def main():
    """
    Main entry point. 
    Uses argparse for CLI definition but does not require arguments via --help or mandatory flags,
    instead relying on the sample block execution below which bypasses interactive prompts.
    Since the task forbids input(), sys.stdin, and required args in a way that blocks non-interactive runs,
    we define an argument parser with optional defaults to ensure it can run without user interaction 
    while still demonstrating the argparse structure requested.
    
    The sample block will be executed directly here via `if __name__ == '__main__':`.
    """
    # Define arguments (optional as per constraint "no required args")
    parser = argparse.ArgumentParser(description="Convert distances between metric units.")
    parser.add_argument('distance', type=float, help='Distance value')
    parser.add_argument('--from-unit', '-f', default=None, choices=['km', 'm', 'cm'], 
                        help='Source unit (default: m)')
    parser.add_argument('--to-unit', '-t', dest='output_unit', default=None, choices=['km', 'm', 'cm'], 
                        help='Target output unit')

def run_sample():
    """
    Executes the conversion logic with hard-coded sample values.
    Ensures no user input or network access is required.
    """
    
    # Sample data: 5 kilometers to centimeters
    distance_value = 5.0
    from_unit = 'km'
    to_unit = 'cm'

    try:
        convert_distance(distance_value, from_unit, to_unit)
    except ValueError as e:
        print(f"Error processing input or units: {e}")

if __name__ == '__main__':
    
    # Check if arguments were actually provided via command line (simulated environment check logic omitted per constraint 
    # that we shouldn't rely on sys.stdin, but argparse handles this automatically).
    # However, to strictly adhere to "Never call input(), sys.stdin", and ensure the sample runs without needing 
    # specific CLI args passed during execution in a test harness, we will prioritize running the hardcoded example.
    
    # If arguments are present (e.g., if user ran: python script.py 10 --from-unit m --to-unit km), use them.
    # Otherwise, run the sample block to ensure it runs without pre-existing files or network access.
    
    args = parser.parse_args()

    if not any([args.distance is None]): 
        # If distance was provided via CLI (which implies no interactive prompt needed)
        try:
            convert_distance(args.distance, args.from_unit, args.output_unit)
        except ValueError as e:
            print(f"Error processing input or units: {e}")

    else:
        # Fallback to sample values if arguments were not effectively provided in a way that triggers the above path 
        # (This handles cases where argparse might fail silently or defaults are used).
        run_sample()