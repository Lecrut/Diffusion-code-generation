import argparse

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Convert volume units."
    )
    
    # Define all possible unit strings for input and output to avoid validation errors later
    ALL_UNITS = {
        "ml", "l", "gal", "qt", "pt"  # ml, liters, gallons (US), quarts, pints
    }

    parser.add_argument(
        "--volume", "-v", 
        type=float, 
        required=False, 
        default=1.0,
        help="The volume to convert."
    )

    parser.add_argument(
        "--from_unit", "-f", 
        choices=list(ALL_UNITS), 
        required=True, 
        dest='start_unit',
        help="Starting unit (e.g., ml, l)."
    )

    parser.add_argument(
        "--to_unit", "-t", 
        choice=list(ALL_UNITS), 
        required=False, 
        default=None, # Will be set to 'l' in the sample block if not provided by user
        help="Target unit (e.g., l)."
    )

    return parser.parse_args()

def convert_volume(volume: float, start_unit: str, target_unit: str) -> float:
    """Convert volume from one unit to another using liters as a base."""
    
    # Base conversion factors relative to 1 liter (l = 1.0)
    BASE_FACTORS = {
        "ml": 0.001,      # 1 ml = 0.001 l
        "l": 1.0,         # 1 l = 1.0 l
        "gal": 3.78541,   # 1 gal (US) ≈ 3.78541 l
        "qt": 0.946353,   # 1 qt (US) ≈ 0.946353 l
        "pt": 0.473176    # 1 pt (US) ≈ 0.473176 l
    }

    try:
        factor_start = BASE_FACTORS[start_unit]
        factor_target = BASE_FACTORS[target_unit]
        
        # Convert to base unit then to target unit
        converted_volume_l = volume * (factor_start / factor_target)
        return rounded(converted_volume_l, 6)

    except KeyError as e:
        raise ValueError(f"Invalid unit provided. Available units are {list(BASE_FACTORS.keys())}") from e

def rounded(value: float, decimals: int) -> float:
    """Round a number to the specified decimal places."""
    return round(value, decimals)

if __name__ == '__main__':
    
    # Hard-coded sample values as per requirements (no user input or network access needed)
    SAMPLE_VOLUME = 1.0
    SAMPLE_START_UNIT = "ml"
    SAMPLE_TARGET_UNIT = "l"

    try:
        args = parse_arguments()
        
        if not args.volume:
            # Use the sample volume since argparse didn't get one from CLI
            vol_to_convert = SAMPLE_VOLUME
        else:
            vol_to_convert = args.volume
        
        start_unit_used = args.start_unit
        
        if not args.to_unit:
            # If target unit wasn't provided on command line, use the sample value
            target_unit_used = "l" 
        else:
            target_unit_used = args.to_unit

        result = convert_volume(vol_to_convert, start_unit_used, target_unit_used)
        
        print(f"{vol_to_convert} {start_unit_used} is equal to {result:.6f} {target_unit_used}")

    except ValueError as e:
        # Handle invalid unit errors gracefully without crashing the whole script if possible (though task says robust CLI)
        # Since we are using argparse with choices, this block might not be reached unless internal logic fails.
        print(f"Error: {e}", file=__import__('sys').stderr)