def convert_kilometers_to_miles(km: float) -> float:
    """Convert kilometers to miles using a standard conversion factor."""
    return km * 0.621371

def validate_float(input_str: str) -> bool:
    """Check if the input string is a valid floating-point number."""
    try:
        float(input_str)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user interaction.
    km_value = 100
    
    print(f"Input value (km): {km_value}")

    try:
        miles_result = convert_kilometers_to_miles(km_value)
        print(f"{km_value} kilometers is equal to {miles_result:.2f} miles")
    except Exception as e:
        # This block handles potential errors during conversion, though unlikely with valid input.
        print(f"An error occurred during calculation: {e}")