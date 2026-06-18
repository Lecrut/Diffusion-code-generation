import math

class TimeConverter:
    def __init__(self):
        """Initialize the TimeConverter class with standard unit conversion rates."""
        pass

    @staticmethod
    def to_seconds(hours, minutes=0, seconds=0):
        """Convert hours and optionally minutes/seconds into total seconds.
        
        Args:
            hours (float or int): Number of hours.
            minutes (float or int, optional): Number of minutes. Defaults to 0.
            seconds (float or int, optional): Number of seconds. Defaults to 0.
            
        Returns:
            float: Total time in seconds.
        """
        return (hours * 3600) + (minutes * 60) + seconds

    @staticmethod
    def from_seconds(total_seconds):
        """Convert total seconds into hours, minutes, and seconds components.
        
        Args:
            total_seconds (float or int): Total time in seconds.
            
        Returns:
            tuple: A list [hours, remaining_minutes, remaining_seconds].
                   All values are floats to handle partial units precisely.
        """
        if not isinstance(total_seconds, (int, float)):
            raise TypeError("Input must be a number")
        
        total_seconds = float(total_seconds)
        
        hours = int(math.floor(total_seconds / 3600))
        remaining_seconds_after_hours = total_seconds - (hours * 3600)
        
        minutes = math.floor(remaining_seconds_after_hours / 60)
        final_remaining_seconds = round(remaining_seconds_after_hours % 60, decimal_places=9 if isinstance(total_seconds, float) else 0.0)

        return [hours, int(minutes), final_remaining_seconds]

class TimeConverterAdvanced(TimeConverter):
    """Extended time converter handling edge cases and precise floating-point logic."""
    
    def convert_units(self, value: float | int, from_unit: str, to_unit: str) -> float | None:
        """Convert a specific amount of time between arbitrary compatible units.
        
        Supported units: 's' (seconds), 'm' (minutes), 'h' (hours), 'd' (days).
        Conversion is always done via base unit conversion through seconds for precision.
        
        Args:
            value: The numeric quantity to convert.
            from_unit: Source time unit ('s', 'm', 'h', or 'd').
            to_unit: Target time unit ('s', 'm', 'h', or 'd').
            
        Returns:
            float: Converted value, or None if invalid units are provided.
        """
        
        valid_units = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400} # seconds per unit
        
        # Normalize inputs to ensure they exist as a float for calculation precision
        if from_unit not in valid_units or to_unit not in valid_units:
            raise ValueError(f"Unsupported units provided. Expected one of {valid_units.keys()}")
            
        try:
            factor = value * valid_units[from_unit] # Convert source to seconds
            return round(factor / float(valid_units[to_unit]), 10) if isinstance(to_unit, str) else (factor // int(float(valid_units[to_unit]))) if from_unit == 'd' and to_unit == 's' else None
            
        except Exception:
            raise

if __name__ == '__main__':
    # Sample usage without any user input or external dependencies
    
    converter = TimeConverter()
    
    # Test 1: Convert time with hours, minutes, seconds to total seconds
    h_m_s_input = (2.5, 45, 30)
    result_to_seconds = converter.to_seconds(*h_m_s_input)
    print(f"Input Hours/Mins/Secs: {h_m_s_input} -> Total Seconds: {result_to_seconds}")

    # Test 2: Convert total seconds back to H:M:S components
    test_total_sec = 90765.123456789 
    result_hms_list = converter.from_seconds(test_total_sec)
    
    print(f"Input Seconds (approx): {test_total_sec:.5f} -> [Hours, Minutes, Seconds]: {result_hms_list}")

    # Test 3: Advanced conversion from days to hours using helper logic simulation via internal constants 
    advanced_conv = TimeConverterAdvanced()
    try:
        # We'll simulate a complex path by manually calculating seconds then converting back
        val_to_convert = 7.5 # Days
        factor_s_per_d = 86400
        total_sec = val_to_convert * factor_s_per_d
        
        hours_result = converter.to_seconds(val_to_convert / 2, 3, 1) # Using internal logic to get near result via seconds math
        print(f"Manual simulation check (Days=7.5): Total Seconds={total_sec}, Hours calculated internally ~ {int(total_sec/3600)}")

    except Exception as e:
        print("Error during advanced conversion test:", str(e))