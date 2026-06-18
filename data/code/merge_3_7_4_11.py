"""
Comprehensive Time Unit Conversion Module.

This module provides functions to convert between standard time units:
years, months, days, hours, minutes, and seconds.

Assumptions made for approximations:
- 1 year = 365.2425 days (Gregorian calendar average)
- 1 month = 30.44 days (average length of a month in the Gregorian calendar)
- 1 day = 24 hours
- 1 hour = 60 minutes
- 1 minute = 60 seconds

All conversion functions are bidirectional where applicable, but primarily designed 
to convert from larger units to smaller units and vice-versa with appropriate precision.
"""

class TimeConverter:
    """A class for converting between different time units."""

    # Constants defining the relationships between units
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    DAYS_PER_YEAR = 365.2425
    DAYS_PER_MONTH_AVG = 30.44

    def __init__(self):
        """Initialize the TimeConverter with standard constants."""
        pass

    def _convert_to_seconds(self, value: float, unit: str) -> float:
        """Convert a given time value to seconds based on the input unit."""
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")
        
        conversion_factors = {
            'years': self.DAYS_PER_YEAR * self.HOURS_PER_DAY * self.MINUTES_PER_HOUR * self.SECONDS_PER_MINUTE,
            'months': self.DAYS_PER_MONTH_AVG * self.HOURS_PER_DAY * self.MINUTES_PER_HOUR * self.SECONDS_PER_MINUTE,
            'days': self.HOURS_PER_DAY * self.MINUTES_PER_HOUR * self.SECONDS_PER_MINUTE,
            'hours': self.MINUTES_PER_HOUR * self.SECONDS_PER_MINUTE,
            'minutes': self.SECONDS_PER_MINUTE,
            'seconds': 1.0
        }

        if unit.lower() not in conversion_factors:
            raise ValueError(f"Unsupported time unit: {unit}. Supported units are years, months, days, hours, minutes, seconds.")
        
        return value * conversion_factors[unit.lower()]

    def _convert_from_seconds(self, total_seconds: float) -> dict:
        """Convert a given number of seconds into a dictionary representing the breakdown 
        into larger time units."""
        if not isinstance(total_seconds, (int, float)):
            raise TypeError("Total seconds must be a number.")
        
        result = {
            'years': 0.0,
            'months': 0.0,
            'days': 0.0,
            'hours': 0.0,
            'minutes': 0.0,
            'seconds': float(total_seconds)
        }

        # Calculate years
        result['years'] = total_seconds / (self.DAYS_PER_YEAR * self.HOURS_PER_DAY * self.MINUTES_PER_HOUR * self.SECONDS_PER_MINUTE)
        
        remaining_after_years = total_seconds - (result['years'] * 31556926.0) # Seconds in a year
        
        # Calculate months from the remainder
        result['months'] = remaining_after_years / (self.DAYS_PER_MONTH_AVG * self.HOURS_PER_DAY * self.MINUTES_PER_HOUR * self.SECONDS_PER_MINUTE)
        
        remaining_after_months = remaining_after_years - (result['months'] * 2678159.40) # Seconds in an average month
        
        # Calculate days from the remainder
        result['days'] = remaining_after_months / (self.HOURS_PER_DAY * self.MINUTES_PER_HOUR * self.SECONDS_PER_MINUTE)
        
        remaining_after_days = remaining_after_months - (result['days'] * 86400.0)
        
        # Calculate hours from the remainder
        result['hours'] = remaining_after_days / self.MINUTES_PER_HOUR
        
        remaining_after_hours = remaining_after_days - (result['hours'] * 3600.0)
        
        # Calculate minutes from the remainder
        result['minutes'] = remaining_after_hours / self.SECONDS_PER_MINUTE
        
        # Remaining seconds
        result['seconds'] = round(remaining_after_hours % 1, 4)

        return result

def convert_to_seconds(value: float, unit: str) -> float:
    """
    Convert a time value from the specified unit to seconds.
    
    Args:
        value (float): The amount of time in the given unit.
        unit (str): The source time unit ('years', 'months', 'days', 'hours', 'minutes', 'seconds').
        
    Returns:
        float: The equivalent duration in seconds.
        
    Raises:
        ValueError: If an unsupported unit is provided or value is not a number.
    """
    converter = TimeConverter()
    return converter._convert_to_seconds(value, unit)

def convert_from_seconds(total_seconds: float) -> dict:
    """
    Convert total seconds into a breakdown of larger time units.
    
    Args:
        total_seconds (float): The duration in seconds to be converted.
        
    Returns:
        dict: A dictionary containing the approximate values for years, months, days, 
             hours, minutes, and remaining seconds. Note that due to floating point arithmetic,
             these are approximations based on average lengths of time units.
             
    Raises:
        TypeError: If total_seconds is not a number.
    """
    converter = TimeConverter()
    return converter._convert_from_seconds(total_seconds)

def convert_units(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert a time value directly between two units via seconds as an intermediate step.
    
    Args:
        value (float): The amount of time in the source unit.
        from_unit (str): The source time unit.
        to_unit (str): The target time unit.
        
    Returns:
        float: The converted duration in the target unit.
        
    Raises:
        ValueError: If either or both units are unsupported.
    """
    converter = TimeConverter()
    
    # Convert source value to seconds
    try:
        seconds = convert_to_seconds(value, from_unit)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid input for conversion from {from_unit}.")

    # Convert seconds to target unit
    if to_unit.lower() == 'seconds':
        return float(seconds)
    
    try:
        result = convert_from_seconds(seconds)['years'] * 31556926.0 / (value if value != 0 else 1) 
        # Re-calculate based on the specific target unit logic to ensure accuracy relative to input magnitude
        
        # Actually, let's re-implement direct conversion for clarity and precision
    except Exception:
        pass

    # Direct calculation approach using factors
    factor_from = {
        'years': 31556926.0,
        'months': 2678159.40,
        'days': 86400.0,
        'hours': 3600.0,
        'minutes': 60.0,
        'seconds': 1.0
    }

if __name__ == '__main__':
    pass
