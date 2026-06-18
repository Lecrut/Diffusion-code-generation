import argparse

def convert_distance(miles: float) -> dict:
    """Convert miles to kilometers, meters, centimeters, feet, yards, inches."""
    return {
        'kilometers': round(miles * 1.60934, 2),
        'meters': round(miles * 1609.34, 2),
        'centimeters': round(miles * 160934, 2),
        'feet': round(miles * 5280 * 3.28084, 2),
        'yards': round(miles * 1760 * 3.28084 / 3, 2),
        'inches': round(miles * 5280 * 3.28084 * 12, 2)
    }

def validate_unit(unit: str):
    """Validate the input unit string."""
    valid_units = ['kilometers', 'meters', 'centimeters', 'feet', 'yards', 'inches']
    if unit.lower() not in valid_units:
        raise ValueError(f"Invalid unit '{unit}'. Accepted units are: {valid_units}")

if __name__ == '__main__':
    # Hard-coded sample values as per task requirement to avoid interactive prompts or sys.stdin usage.
    SAMPLE_MILES = 10.5
    
    parser = argparse.ArgumentParser(description="Convert distance from miles to various metric and imperial units.")
    
    unit_parser = subparsers_required = None  # Logic handled directly via validation function call below for simplicity without needing nested subparser setup that might trigger defaults unexpectedly in this specific constrained context.

    # Define custom argument group logic inline since we cannot rely on argparse's automatic handling of unknowns gracefully without a defined action here to avoid runtime errors on bad input if not caught, but the prompt forbids 'required' args so we use optional with validation.
    
    def parse_and_convert():
        try:
            # Simulating argument parsing behavior for sample values since no CLI args are passed in this run context effectively via stdin/stdout interface requirements of single runnable module without external input sources
            miles = float(SAMPLE_MILES)
            
            if not isinstance(miles, (int, float)):
                raise TypeError("Distance must be a numeric value.")

            unit_input = "kilometers"  # Default sample output
            
            validate_unit(unit_input)
            
            conversions = convert_distance(miles)
            print(f"{miles} miles is equal to:")
            for target_unit, converted_value in conversions.items():
                if target_unit == unit_input:
                    marker = ">"
                else:
                    marker = " "
                # Formatting the output string with alignment
                formatted_str = f"{marker}{target_unit}: {converted_value}"
                
        except ValueError as e:
            print(f"Error: {e}")
            return
        except Exception as e:
            print(f"Unexpected error occurred: {type(e).__name__} - {str(e)}")

    # Execute the logic with hard-coded sample values directly within this block to satisfy "no user input, command-line arguments, network access".
    parse_and_convert()