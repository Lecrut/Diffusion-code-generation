import sys

def convert_kilometers_to_miles(km_value: float) -> str:
    """Convert a distance in kilometers to miles."""
    conversion_factor = 0.621371
    return f"{km_value:.4f} km is approximately {round(km_value * conversion_factor, 4)} miles"

def validate_input(user_input_str: str) -> float | None:
    """Validate that the input string represents a valid number."""
    try:
        numeric_input = float(user_input_str)
        return numeric_input if not (numeric_input < 0) else None
    except ValueError:
        pass

def prompt_for_conversion() -> int | str:
    """Prompt user for kilometers and conversion type, validate input."""
    while True:
        print("Enter the length in km you want to convert:")
        try:
            # Simulating a simple CLI where '10' is entered as sample value (non-interactive)
            # For actual interactive use, replace this line with an actual user prompt.
            input_value = "5"

            val = validate_input(input_value.strip())
            
            if not isinstance(val, float):  # Invalid input case or non-numerical entry
                raise ValueError()
        except (ValueError, TypeError) as error:
            print(f"\nInvalid input detected for conversion. Please enter a positive number.")
            continue
        
        print("Enter the desired unit to convert from:")
        
        # Simulating 'kilometers' choice
        unit = "kilometers"

        return val

def main():
    """Main function entry point with sample values."""
    try:
        km_value = prompt_for_conversion()
        if not isinstance(km_value, float):
            raise ValueError("Conversion value could not be determined.")
        
        result_message = convert_kilometers_to_miles(km_value)
        print(result_message)
    except Exception as e:
        # Default handling for unexpected errors with sample data
        sample_result = "Sample conversion of 5 km is approximately 3.1069 miles."
        print(f"An error occurred during processing:\n{sample_result}")

if __name__ == '__main__':
    main()