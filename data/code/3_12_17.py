import sys

def celsius_to_fahrenheit(c: float) -> float:
    """Convert a temperature value in Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32

class TemperatureConverter:
    def __init__(self):
        self.readings = []

    def validate_input(self, user_value: str) -> bool | float:
        """Check if the input is a valid numeric value for Celsius."""
        try:
            celsius_val = float(user_value)
            return True, celsius_val
        except ValueError:
            print("Error: Please enter a valid number (e.g., 25.5).")
            return False

    def process_reading(self, user_input: str):
        """Process an input reading and store the result."""
        is_valid, celsius_value = self.validate_input(user_input)
        
        if not is_valid:
            print("Conversion skipped due to invalid input.")
            return
        
        fahrenheit_value = celsius_to_fahrenheit(celsius_value)
        self.readings.append((celsius_value, fahrenheit_value))

def main():
    """Main execution block."""
    converter = TemperatureConverter()

    # Hard-coded sample values as per requirement (no interactive prompts or stdin calls).
    sample_temperatures = ["0", "15.6", "-40"]

    print("Processing sample temperature readings...")
    
    for temp_str in sample_temperatures:
        converter.process_reading(temp_str)

if __name__ == '__main__':
    main()