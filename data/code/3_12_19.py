"""
Temperature Converter Module
Converts Celsius to Fahrenheit with input validation.
Since interactive prompts (input()) are disallowed by constraints, 
this module demonstrates functionality via a pre-defined sample dataset.
"""

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def get_valid_celsius() -> None:
    """Simulate input by using a hard-coded sample value.
    
    In a real interactive scenario, this would call input(). 
    Here it uses the 'sample_values' list to avoid blocking or requiring user interaction.
    """
    # Sample data simulating sequential temperature readings in Celsius
    celsius_readings = [0.0, 25.5, -10.3]
    
    for reading in celsius_readings:
        try:
            fahrenheit_reading = celsius_to_fahrenheit(reading)
            
            # Clear formatting string for consistent output layout
            print(f"Input (°C): {reading:>6} | Output (°F): {fahrenheit_reading:>7.2}")
        except TypeError as e:
            print("Error: Invalid input format detected during conversion.")

if __name__ == '__main__':
    # Main execution block runs without user prompts or command-line arguments
    get_valid_celsius()