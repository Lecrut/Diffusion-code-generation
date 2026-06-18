"""
Script to calculate the difference between two volume measurements.
This module demonstrates robust error handling for non-numeric input 
while operating entirely without user interaction, command-line arguments,
network access, or file I/O beyond a hardcoded execution block.
"""

class VolumeCalculator:
    """A class encapsulating logic to compute differences between volumes."""

    def __init__(self):
        self.volume_a = 0
        self.volume_b = 0

    def set_volume(self, value_str: str) -> bool:
        """
        Attempts to parse a string into a float volume measurement.
        
        Args:
            value_str (str): String representation of the volume.
            
        Returns:
            bool: True if successful conversion and assignment occurred; 
                  False otherwise. Sets internal state on success only.
        """
        try:
            # Validate that input is not empty or purely whitespace before attempting float() call
            value_str = value_str.strip()
            if not value_str:
                return False
            
            self.volume_a = float(value_str)
            return True
        except ValueError:
            # Handle cases where the string cannot be converted to a number (e.g., "abc", 12.5ab")
            pass
        
    def calculate_difference(self, volume_b_float: float) -> float:
        """
        Calculates and returns the difference between stored volume A 
        and an externally provided floating point value for B.
        
        Args:
            volume_b_float (float): The numeric value of the second measurement.
            
        Returns:
            float: Result of self.volume_a - volume_b_float.
            Raises ValueError if internal state is invalid or input is not a number.
        """
        # Ensure current stored volumes are valid numbers before computation
        try:
            diff = self.volume_a - volume_b_float
            return diff
        except TypeError as e:
            raise ValueError("Internal calculation error: Invalid numeric states detected.") from e

def parse_volume(input_str: str) -> float | None:
    """
    Static helper function to safely convert a string input into a floating-point number.
    
    Args:
        input_str (str): The raw user or system input string.
        
    Returns:
        float | None: The parsed float value if successful; 
                      None if the conversion fails due to non-numeric content.
    """
    try:
        return float(input_str)
    except ValueError:
        # Explicitly catch and handle all ValueErrors (invalid literals, formatting issues)
        pass
    
    return None

def run_sample_calculation():
    """
    Executes a self-contained calculation using hard-coded sample values.
    
    This block replaces any potential input() calls or argument parsing requirements.
    It demonstrates the calculator's functionality with predefined data sets 
    simulating two distinct volume measurements (e.g., 10 liters and 35 gallons).
    """
    
    # Initialize calculation engine
    calc = VolumeCalculator()

    # Sample inputs representing hypothetical measurements
    sample_measurement_1_str = "12.5"
    sample_measurement_2_str = "-4.7"

    print(f"[Sample Run] Processing Measurement A: '{sample_measurement_1_str}'")
    
    # Attempt to set first measurement
    if not calc.set_volume(sample_measurement_1_str):
        raise RuntimeError("Failed to initialize primary volume value.")

    print(f"[Success] Primary Volume Set To: {calc.volume_a}")

    sample_diff_value = 5.0
    
    # Compute final difference between Sample A and an arbitrary constant B for demonstration
    try:
        result = calc.calculate_difference(sample_diff_value)
        
        formatted_result = f"{result:.2f}" if isinstance(result, float) else str(result)
        print(f"[Output] Calculated Difference (12.5 - 5.0): {formatted_result}")

    except ValueError as ve:
        # Graceful handling of calculation logic errors
        error_msg = f"An unexpected arithmetic issue occurred during sample execution."
        raise RuntimeError(error_msg) from ve

if __name__ == '__main__':
    run_sample_calculation()