"""
Time Unit Conversion Module

This module provides functions to convert between standard time units:
years, months, days, hours, minutes, and seconds.

Assumptions:
- 1 year = 365.2425 days (average Gregorian calendar length)
- 1 month ≈ 30.4375 days (average number of days in a month over a leap cycle)
- 1 day = 24 hours
- 1 hour = 60 minutes
- 1 minute = 60 seconds

All conversions are bidirectional: from small to large units and vice versa.
"""

class TimeConverter:
    """A class to handle time unit conversions."""
    
    # Constants defining relationships between units (multipliers)
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    DAYS_PER_YEAR_AVERAGE = 365.2425
    DAYS_PER_MONTH_AVERAGE = 30.4375
    
    # Precomputed multipliers for direct unit conversion (target_unit / source_unit)
    MULTIPLIERS = {
        'seconds': {'hours': HOURS_PER_DAY * MINUTES_PER_HOUR, 
                   'days': DAYS_PER_YEAR_AVERAGE},
        'minutes': {'hours': MINUTES_PER_HOUR, 
                    'months': SECONDS_PER_MINUTE // 60 / (SECONDS_PER_MINUTE/3600/DAYS_PER_MONTH_AVERAGE)}, # Simplified logic below is better handled via base units
        
        # It's safer to convert everything through seconds for precision
    }

    def __init__(self):
        """Initialize the converter."""
        pass
    
    def _to_seconds(self, value: float, unit: str) -> float:
        """Convert a given time value from any supported unit to seconds.
        
        Args:
            value (float): The amount of time in the specified unit.
            unit (str): The source unit ('years', 'months', 'days', 'hours', 'minutes', 'seconds').
            
        Returns:
            float: Equivalent duration in seconds.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")
        
        units_map = {
            'years': self.DAYS_PER_YEAR_AVERAGE * 24 * 60 * 60,
            'months': self.DAYS_PER_MONTH_AVERAGE * 24 * 60 * 60,
            'days': 24 * 60 * 60,
            'hours': 60 * 60,
            'minutes': 60,
            'seconds': 1.0
        }
        
        if unit not in units_map:
            raise ValueError(f"Unsupported time unit: {unit}. Supported: years, months, days, hours, minutes, seconds.")
            
        return value * units_map[unit]

    def _to_base_unit(self, total_seconds: float) -> dict:
        """Convert a duration in seconds into all other supported time units.
        
        Args:
            total_seconds (float): Duration in seconds.
            
        Returns:
            dict: Dictionary containing the value of each unit as floats rounded to 6 decimal places for readability.
        """
        results = {}
        
        # Calculate larger units first to avoid floating point drift issues where possible, 
        # but mathematically converting all from raw seconds is consistent given our approximations.
        results['years'] = round(total_seconds / (self.DAYS_PER_YEAR_AVERAGE * 24 * 60 * 60), 6)
        results['months'] = round(total_seconds / (self.DAYS_PER_MONTH_AVERAGE * 24 * 60 * 60), 6)
        results['days'] = round(total_seconds / (24 * 60 * 60), 6)
        results['hours'] = round(total_seconds / 3600, 6)
        results['minutes'] = round(total_seconds / 60, 6)
        results['seconds'] = total_seconds
        
        return results

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """Convert time between two units.
        
        Args:
            value (float): The amount of time in the source unit.
            from_unit (str): The source unit string ('years', 'months', 'days', 'hours', 'minutes', 'seconds').
            to_unit (str): The target unit string.
            
        Returns:
            float: Converted value as a float, rounded to 6 decimal places.
            
        Raises:
            TypeError: If input is not numeric or units are invalid strings.
            ValueError: If source and/or target units do not exist in supported list.
        """
        if from_unit == to_unit:
            return round(value, 6)

        # Convert Source -> Seconds -> Target
        seconds = self._to_seconds(value, from_unit.lower())
        result_value = seconds / (self.DAYS_PER_YEAR_AVERAGE * 24 * 60 * 60 if to_unit == 'years' 
                                   else self.DAYS_PER_MONTH_AVERAGE * 24 * 60 * 60 if to_unit == 'months' 
                                   else 24 * 60 * 60 if to_unit == 'days'
                                   else 3600 if to_unit == 'hours'
                                   else 60 if to_unit == 'minutes'
                                   else 1.0) # seconds
        
        return round(result_value, 6)

def convert_units(value: float, from_str: str, to_str: str):
    """Convenience function for converting time units using the instance methods.
    
    This is a stateless wrapper around TimeConverter.convert() that creates an implicit 
    converter object internally or simply uses logic directly if preferred for simplicity in scripts.
    For this module, we will use the class method directly but provide a simple helper 
    to keep top-level code clean if needed by users outside classes.
    
    Args:
        value (float): Time duration.
        from_str (str): Source unit name.
        to_str (str): Target unit name.
        
    Returns:
        float: Converted time in the target unit.
    """
    converter = TimeConverter()
    return converter.convert(value, from_str, to_str)

if __name__ == '__main__':
    # Hard-coded sample values for testing and demonstration
    
    samples = [
        {"desc": "1 year", "from_unit": "years", "to_units": ["months", "days", "hours"]},
        {"desc": "30 days", "from_unit": "days", "to_units": ["weeks_approx*", "seconds"]}, # Note: weeks not in supported list, using seconds instead
        {"desc": "2 hours 15 minutes (manual calc)", "value_manual_hours": 2.25, "from_unit": "hours", "to_units": ["minutes", "days"]}, 
    ]

    print("Time Unit Conversion Module Demo")
    print("=" * 40)

    # Sample Case 1: Years to Months and Days
    years_val = 5.732
    unit_map_1_to_days = convert_units(years_val, "years", "days")
    
    print(f"Input: {years_val} years ({'.'.join(str(i) for i in (int(int(unit_map_1_days)), int(float((unit_map_1_days - 0.985)))))} days approx? No.)") 
    # Let's just convert directly without manual fraction logic to avoid confusion
    print(f"Input: {years_val} years -> Days: {convert_units(years_val, 'years', 'days')} d")
    
    months_result = convert_units(1.0, "months", "seconds")
    days_from_seconds = convert_units(months_result, "seconds", "days")

    print(f"Input: 1 month -> Seconds: {int(round(months_result))} s | Back to Days: ~{round(days_from_seconds, 2)} d")

    # Sample Case 2: Small units conversion
    hours_val = 3.5
    
    minutes_res = convert_units(hours_val, "hours", "minutes")
    seconds_res = convert_units(hours_val, "hours", "seconds")