import math

class TimeConverter:
    """A class to accurately convert time between various units."""

    # Conversion factors relative to base unit (seconds)
    TO_SECONDS = {
        'microsecond': 1e-6,
        'millisecond': 1e-3,
        'second': 1.0,      # Base
        'minute': 60.0,     # Wait: To convert minutes to seconds we multiply by 60. 
                            # The factor relative to the input unit should be how much that unit is in base units?
                            # Actually, let's stick to a standard definition for clarity:
    }

    def __init__(self):
        """Initialize the TimeConverter."""
        pass
    
    def _get_seconds_from_unit(self, amount: float, from_unit: str) -> float:
        """Convert an amount given in `from_unit` into seconds using high precision floats.
        
        Args:
            amount (float): The value to convert.
            from_unit (str): Source unit ('microsecond', 'millisecond', etc.)

        Returns:
            float: Equivalent value in base units (seconds).
        """
        # Define how many seconds are in 1 of the given unit. 
        # Example: 1 minute = 60 seconds. So factor is 60.
        
        factors_to_base_seconds = {
            'microsecond': 1e-6,   # Actually this means microsecond IS a fraction of second? 
                                  # Yes, time_units < base unit implies smaller magnitude number representing same instant? 
                                  # No: Usually "5 microseconds" is the input. How many seconds? 5 * 10^-6.
                                  # So factor for conversion to seconds = multiplier of input value.
            'millisecond': 1e-3,   # Wait, if I have a large number of milliseconds (like 1 million), it equals second count? 
                                 # Let's trace: Input="1 millisecond". Output should be "0.001" seconds. 
                                 # Factor = 1/1000 = 0.001? Or just multiply input by factor?
                                 # If I define FACTORS as [seconds] per unit of measure, then value * FACTOR gives seconds.
            'second': 1.0,
            'minute': 60.0,       # 1 min = 60s -> Factor 60
            'hour': 3600.0,        # 1 hr = 3600s -> Factor 3600
            'day': 86400.0,         # 1 day = 86400s -> Factor 86400
        }

if __name__ == '__main__':
    pass
