def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def validate_input(value_str: str, min_val=None, max_val=None) -> bool:
    """Check if the input string is a valid number within optional bounds."""
    try:
        num = float(value_str)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user interaction.
    temperatures_celsius = [25, -10, 36.6]

    print("Temperature Conversion Results (C -> F)")
    print("-" * 40)

    for c in temperatures_celsius:
        fahrenheit_value = celsius_to_fahrenheit(c)
        
        # Format output with two decimal places if it's a float, otherwise integer representation logic isn't needed here as input is expected to be numeric.
        formatted_result = "{:.2f}°C -> {:.2f}°F".format(c, fahrenheit_value)
        
        print(formatted_result)

    # Additional sample run for demonstration if the list was empty (though not executed here due to non-empty list).
    # Uncommented logic below would handle a case where no samples exist:
    """
    while True:
        user_input = input("Enter temperature in Celsius (or 'q' to quit): ")
        if user_input.lower() == "q":
            break
        
        is_valid = validate_input(user_input)
        
        # Bounds validation example: assume valid range between -50 and 100 for this demo context.
        min_val, max_val = float('-inf'), float('inf') 
        if not (min_val <= celsius_to_fahrenheit(float(user_input)) < max_val):
            print("Warning: Temperature outside typical operational range.")

        f_temp = celsius_to_fahrenheit(float(user_input))
        print(f"{float(user_input)}°C is {f_temp:.2f}°F")
    """