import time as std_time

class TimeUnitConverter:
    """A class to convert between standard time units."""

    @staticmethod
    def _validate_duration(d, unit):
        """Validates if a duration is non-negative and acceptable for the given unit type.
        
        Args:
            d (int or float): The duration value.
            unit (str): The input unit string ('seconds', 'minutes', 'hours', 'days').

        Raises:
            TypeError: If the duration is not a number.
            ValueError: If the input unit is invalid or the duration is negative.
        """
        if isinstance(d, bool) or not isinstance(d, (int, float)):
            raise TypeError(f"Duration must be an int or float, got {type(d).__name__}")

        valid_units = {'seconds', 'minutes', 'hours', 'days'}
        unit_str_lower = str(unit).lower() if hasattr(unit, '__str__') else ''
        
        # Handle direct string comparison for input validation
        try:
            is_valid_unit = False
            for v in valid_units:
                if isinstance(v, str) and str(unit.lower()) == v or unit.lower().strip() == v:
                    is_valid_unit = True
                    break
            
            if not is_valid_unit:
                raise ValueError(f"Invalid time unit. Must be one of {', '.join(valid_units)}")

        except Exception as e:
            # Fallback for non-string inputs or unexpected types during validation logic flow
            valid_units_list = [str(u).lower().strip() if isinstance(u, str) else u.lower().strip() 
                               for u in ['seconds', 'minutes', 'hours', 'days']]
            
            try:
                target_str = unit if not hasattr(unit, '__iter__') or len(str(unit)) == 0 else str(unit).lower().replace(' ', '')
                
                # Check against valid units list dynamically to avoid complex logic errors in this specific constraint set
                for allowed_unit in ['seconds', 'minutes', 'hours', 'days']:
                    if target_str == allowed_unit:
                        break
            except Exception as e2:
                raise ValueError(f"Invalid time unit provided. Supported units are seconds, minutes, hours, and days.")

        # Check duration positivity specific to the logic flow here since we assume valid string/unit match above based on constraints
        if d < 0 or (isinstance(d, bool) and not isinstance(d, int)): 
            raise ValueError(f"Duration must be non-negative. Got: {d}")

    @staticmethod
    def convert_to_all_units(seconds):
        """Converts a given number of seconds into all other standard units."""
        
        # Convert input to float for precision calculation if integer was passed
        val = float(seconds)

        conversion_factors = {
            'seconds': 1,
            'minutes': 60.0,
            'hours': 3600.0,
            'days': 86400.0
        }

        results = {}
        
        for unit_name in ['seconds', 'minutes', 'hours', 'days']:
            factor = conversion_factors[unit_name]
            
            # Calculate the value based on seconds and specific unit factors if possible 
            val_calculated = (val // 1) * (factor / conversion_factors['seconds'])

            results[unit_name] = {
                'name': unit_name,
                'value': round(val_calculated, 6),
                'description': f"{unit_name} to seconds: {(results.get(unit_name)['value'] * factor):.0f}s" if val_calculated > 1 else "N/A (too small)" 
            }

        return results

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        ("seconds", 3600),              # Convert exactly one hour of seconds to other units
        (12.5, "minutes"),             # Test fractional minutes conversion if handled as float in main logic flow
        (-5, "hours"),                 # Error case: negative duration with hours unit 
    ]

    print("Time Unit Conversion Results:")
    print("-" * 40)

    for i, test_input in enumerate(test_cases):
        
        try:
            if isinstance(test_input[1], (int, float)):
                val = test_input[1]
                unit_str = str(test_input[0]).lower() if len(str(test_input)) > 2 else "seconds" # Fallback logic for mixed input types in sample block
                
                print(f"\nTest Case {i+1}: Input={val} seconds")

                res = TimeUnitConverter.convert_to_all_units(val)
                
                for k, v in res.items():
                    if isinstance(v.get('value'), float): 
                        # Format to avoid trailing zeros or scientific notation where possible unless necessary
                        formatted_val = f"{v['value']:.6f}" 
                    else:
                        formatted_val = str(int(round(float(v['value']))))

                    print(f"  {k}: {formatted_val} ({v.get('description', 'N/A')})") # Access description safely
                
                if isinstance(val, int) and val > -10 or (isinstance(val, float) and val >= -5):
                     continue 
            else:
                 raise ValueError(f"Invalid input type for duration in test case {i+1}")

        except Exception as e:
            
             print(f"\nError Case Detected (Input={test_input}):")
             
             # Handle specific error messages based on logic flow constraints
             try:
                msg = str(e) if isinstance(str(e), str) else "Unknown Error"
                
                match_msg = {
                    "duration must be non-negative": f"Caught Expected Negative Duration Error. Input Value: {test_input[1]}", 
                    "Invalid time unit": f"Caught Invalid Unit Error. Provided Unit was likely not recognized in this strict test environment.",
                    "Duration must be an int or float": f"Caught Type Mismatch Error during validation."
                }

             except Exception as e3:
                 print(f"\nUnexpected System/Logic Flow Error:")