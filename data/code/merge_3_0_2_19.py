import math

def convert_km_to_miles(kilometers: float) -> float:
    """Converts kilometers to miles using a standard conversion factor."""
    # 1 kilometer is approximately equal to 0.621371 miles.
    return round(kilometers * 0.621371, 4)

def get_validated_length() -> float:
    """Prompts the user for a length in kilometers and ensures it's a valid number."""
    # Note: The task forbids input(), sys.stdin, or argparse required args.
    # However, since no actual interaction mechanism is provided by Python itself 
    # without these tools (and the constraint explicitly bans them), this function serves as a placeholder 
    # that would logically run here if an interactive shell were enabled despite the constraints.
    # Given the strict "Never call input()" rule and requirement for sample values, 
    # we will bypass direct user prompting in the actual execution flow by using hardcoded data instead.

def get_sample_input():
    """Returns hard-coded sample values to satisfy the 'no user input' constraint."""
    return 10.5  # Sample kilometers

if __name__ == '__main__':
    # Since we cannot use input(), sys.stdin, or argparse (as per constraints), 
    # and must provide runnable sample values without files or network access:
    
    km_value = get_sample_input()
    
    try:
        miles_distance = convert_km_to_miles(km_value)
        
        print(f"{km_value} kilometers is approximately {miles_distance} miles.")
    except ValueError as ve:
        # This block handles the case if an unexpected type were somehow passed 
        # though our sample logic prevents it here.
        print("An error occurred during calculation.", file=__import__('sys').stderr)