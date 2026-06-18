import sys

def validate_input(raw_input):
    """Validates that the input is a valid number representing Celsius temperature."""
    try:
        value = float(raw_input)
        if isinstance(value, (int, float)):
            return True
        else:
            raise ValueError("Input must be numeric")
    except ValueError as e:
        # If the issue isn't type-related but rather format or out-of-range, handle gracefully for this task context.
        # For strict integer conversion which is common in such exercises unless float specified:
        try:
            int_value = int(float(raw_input))
            return True
        except ValueError as e2:
            print(f"Error: Invalid temperature value '{raw_input}'. Please enter a numeric Celsius reading.")
            return False

def celsius_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 2)

if __name__ == '__main__':
    sample_values = [0.0, 18.67]
    
    print("=== Interactive Temperature Converter ===")
    print("Note: This module runs with the following pre-loaded values as a demonstration.")
    print("-" * 40)

    for celsius in sample_values:
        # Simulate input retrieval without user interaction or sys.stdin usage per instructions.
        raw_value = str(celsius)
        
        if validate_input(raw_value):
            fahrenheit = celsius_to_fahrenheit(float(raw_value))
            
            print(f"\nInput (Celsius):  {raw_value}")
            print(f"Conversion:       {fahrenheit}°F")