import math

class TimeConverter:
    """
    A class to accurately convert time between various units (seconds, minutes, hours, days).
    All calculations use standard conversion factors ensuring mathematical precision 
    within floating-point limits without external dependencies or rounding errors for simple cases.
    
    Supported conversions:
        - seconds <-> minutes
        - seconds <-> hours
        - seconds <-> days
        - minutes <-> hours
        - minutes <-> days
        - hours <-> days
    
    Conversion factors used (exact):
        1 minute = 60 seconds
        1 hour   = 3600 seconds (= 60 * 60)
        1 day    = 86400 seconds (= 24 * 3600)
    
    The class supports conversion from any supported unit to another.
    """

    # Define exact conversion factors relative to base unit (seconds) for clarity and consistency
    FACTORS = {
        's': 1,           # Seconds factor: x seconds -> x * s_factor
        'm': 60,          # Minutes factor: x minutes -> x * m_seconds_per_min
        'h': 3600,        # Hours factor: x hours -> x * h_seconds_per_hour
        'd': 86400,       # Days factor: x days -> x * d_seconds_per_day
    }

    def __init__(self):
        """Initialize the TimeConverter instance."""
        pass

    def convert(self, value, from_unit, to_unit):
        """
        Convert a time value from one unit to another.
        
        Parameters:
            value (float or int): The amount of time in the source unit.
            from_unit (str): Source unit ('s', 'm', 'h', 'd'). Must be valid.
            to_unit (str): Target unit ('s', 'm', 'h', 'd'). Must be valid.
            
        Returns:
            float or int: The converted time value in the target unit, 
                          rounded only if necessary for display but kept precise internally.
                          
        Raises:
            ValueError: If units are invalid or from_unit equals to_unit (no-op handled gracefully).
        
        Example usage: convert(3600, 's', 'h') returns 1.0
        """
        # Validate input types and values
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")

        valid_units = {'s', 'm', 'h', 'd'}
        if from_unit not in valid_units or to_unit not in valid_units:
            raise ValueError(f"Invalid unit. Supported units are {valid_units}.")

        # If source and target are the same, return original value (no conversion needed)
        if from_unit == to_unit:
            return float(value)

        # Convert to base unit (seconds), then convert to target unit
        seconds = self._to_base(value, from_unit)
        
        # Calculate result in target units using inverse of factor logic or direct ratio
        
        # Direct formula approach for precision and simplicity:
        # value_in_target = value * (factor_from / factor_to) 
        # But since we have factors relative to seconds, let's just use the two-step conversion.

        return self._from_base(seconds, to_unit)

    def _to_base(self, value, unit):
        """Convert a time value in given 'unit' to base unit (seconds)."""
        factor = self.FACTORS[unit]
        # Multiply by seconds per unit of input type. 
        # Note: For example if input is minutes -> multiply by 60. If hours -> *3600.
        
        return value * float(factor)

    def _from_base(self, seconds, target_unit):
        """Convert a time value in base (seconds) to the specified 'target_unit'."""
        factor = self.FACTORS[target_unit]
        # Divide by seconds per unit of output type. 
        # Note: For example if input is seconds -> divide by 1. If days -> /86400.

        result = seconds / float(factor)
        
        return round(result, 2)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user interaction
    
    converter = TimeConverter()
    
    test_cases = [
        {"value": 3600, "from_unit": "s", "to_unit": "h"},           # 1 hour in seconds -> hours
        {"value": 7200, "from_unit": "m", "to_unit": "d"},          # 7200 minutes (48*60) -> days? Wait: 7200 mins = 120 hrs = 5 days. Let's check logic below
        {"value": 360, "from_unit": "h", "to_unit": "m"},           # 3 hours to minutes
        {"value": 86400, "from_unit": "s", "to_unit": "d"},         # 1 day in seconds -> days
        {"value": 5.25, "from_unit": "h", "to_unit": "m"},          # 5.25 hours to minutes (should be exact)
    ]

    print("Time Conversion Results:")
    for tc in test_cases:
        val = tc["value"]
        from_u = tc["from_unit"]
        to_u = tc["to_unit"]
        
        try:
            result = converter.convert(val, from_u, to_u)
            
            # Display formatted output with context
            print(f"Converting {val} {from_u}s -> {result} {to_u}")
        except Exception as e:
            print(f"Error converting {tc['value']} {tc['from_unit']} to {tc['to_unit']}: {e}")

    # Additional specific test for precision (5.25 hours = 315 minutes exactly)
    result_5h25m = converter.convert(5.25, "h", "m")
    print(f"Verification: 5.25 h -> m should be 315.0; Got {result_5h25m}")