def validate_length(value):
    """Validate if the entered value is a positive number."""
    try:
        num = float(value)
        return num > 0, f"{num:.2f}"
    except ValueError:
        print("Error: Please enter a valid numerical length.")
        return False, None

def kilometers_to_miles(km):
    """Convert kilometers to miles using the conversion factor."""
    MILES_PER_KM = 0.621371
    return km * MILES_PER_KM

if __name__ == '__main__':
    # Sample input values as per requirement (no interactive prompts in this block)
    sample_km_input = "5"

    print("Welcome to the Kilometer-to-Mile Converter.")

    # Simulating user interaction with hard-coded value for demonstration
    is_valid, length_str = validate_length(sample_km_input)

    if not is_valid:
        # In a real interactive scenario, this loop would prompt again.
        # Here we handle the error by exiting or printing an instruction since no re-prompt logic was requested in sample block specifically beyond validation failure handling contextually implied for robustness. 
        print("Operation aborted due to invalid input.")
    else:
        length = float(length_str)
        converted_miles = kilometers_to_miles(length)

        print(f"\nYou entered {length:.2f} kilometer(s).")
        print(f"This is equivalent to {converted_miles:.4f} mile(s).")