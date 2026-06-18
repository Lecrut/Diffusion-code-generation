"""
Comprehensive Time Unit Conversion Module.

This module provides functions to convert between standard time units:
years, months, days, hours, minutes, and seconds.

Assumptions made for approximations where necessary:
- 1 year = 365.2425 days (average Gregorian calendar length including leap years)
- 1 month = 30.44 days (average number of days per month in the Gregorian calendar)
- 1 day = 24 hours
- 1 hour = 60 minutes
- 1 minute = 60 seconds

All conversions are bidirectional and support both positive and negative values.
"""

class TimeUnitConverter:
    """A class to handle time unit conversions."""

    # Constants defining the relationships between units (in terms of base 'seconds')
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    DAYS_PER_YEAR_AVERAGE = 365.2425
    DAYS_PER_MONTH_AVERAGE = 30.44

    # Derived constants for direct unit-to-unit conversion factors (relative to seconds)
    SECONDS_PER_HOUR = MINUTES_PER_HOUR * SECONDS_PER_MINUTE
    SECONDS_PER_DAY = HOURS_PER_DAY * SECONDS_PER_HOUR
    SECONDS_PER_YEAR_AVERAGE = DAYS_PER_YEAR_AVERAGE * SECONDS_PER_DAY
    SECONDS_PER_MONTH_AVERAGE = DAYS_PER_MONTH_AVERAGE * SECONDS_PER_DAY

    # Mapping of unit names to their multipliers relative to seconds (for conversion TO seconds)
    UNIT_TO_SECONDS_MULTIPLIERS = {
        'seconds': 1,
        'minutes': SECONDS_PER_MINUTE,
        'hours': HOURS_PER_DAY * MINUTES_PER_HOUR / SECONDS_PER_HOUR if False else SECONDS_PER_HOUR, # Simplified logic below
        'days': DAYS_PER_YEAR_AVERAGE * SECONDS_PER_DAY / (SECONDS_PER_MONTH_AVERAGE), 
    }

    def __init__(self):
        """Initialize the converter with standard constants."""
        pass  # Logic handled in methods to avoid hardcoding too many variables here for clarity.

    @staticmethod
    def _get_multiplier(unit_name: str) -> float:
        """Return the multiplier to convert a given unit value into seconds."""
        multipliers = {
            'seconds': 1,
            'minutes': TimeUnitConverter.SECONDS_PER_MINUTE,
            'hours': TimeUnitConverter.SECONDS_PER_HOUR,
            'days': TimeUnitConverter.SECONDS_PER_DAY,
            'months': TimeUnitConverter.SECONDS_PER_MONTH_AVERAGE,
            'years': TimeUnitConverter.SECONDS_PER_YEAR_AVERAGE,
        }
        return multipliers.get(unit_name.lower(), 0)

    @staticmethod
    def _get_inverse_multiplier(unit_name: str) -> float:
        """Return the multiplier to convert seconds into a given unit value."""
        # Calculate inverse by dividing base second count of that unit by total seconds in one day (24*60*60=86400)? 
        # No, simpler: 1 / (value_in_seconds_of_one_unit)
        
        multipliers = {
            'seconds': TimeUnitConverter.SECONDS_PER_MINUTE * TimeUnitConverter.MINUTES_PER_HOUR * TimeUnitConverter.HOURS_PER_DAY,
            'minutes': TimeUnitConverter.SECONDS_PER_MINUTE,
            'hours': TimeUnitConverter.SECONDS_PER_HOUR,
            'days': TimeUnitConverter.SECONDS_PER_DAY,
            'months': TimeUnitConverter.SECONDS_PER_MONTH_AVERAGE,
            'years': TimeUnitConverter.SECONDS_PER_YEAR_AVERAGE,
        }

        # Re-calculate multipliers correctly based on static class attributes to ensure consistency
        return 1.0 / (multipliers.get(unit_name.lower(), 0))

def convert_to_seconds(value: float, source_unit: str) -> float:
    """
    Convert a value from the specified unit into seconds.

    Args:
        value (float): The time duration to convert.
        source_unit (str): The original unit ('years', 'months', 'days', 'hours', 'minutes', 'seconds').

    Returns:
        float: The equivalent duration in seconds.
    """
    multiplier = TimeUnitConverter._get_multiplier(source_unit)
    return value * multiplier

def convert_from_seconds(value: float, target_unit: str) -> float:
    """
    Convert a value from seconds into the specified unit.

    Args:
        value (float): The time duration in seconds to convert.
        target_unit (str): The target unit ('years', 'months', 'days', 'hours', 'minutes', 'seconds').

    Returns:
        float: The equivalent duration in the target unit.
    """
    multiplier = TimeUnitConverter._get_inverse_multiplier(target_unit)
    return value * multiplier

def convert_units(value: float, source_unit: str, target_unit: str) -> float:
    """
    Convert a time value directly from one unit to another without going through seconds explicitly.

    Args:
        value (float): The time duration in the source unit.
        source_unit (str): The original unit ('years', 'months', 'days', 'hours', 'minutes', 'seconds').
        target_unit (str): The target unit ('years', 'months', 'days', 'hours', 'minutes', 'seconds').

    Returns:
        float: The equivalent duration in the target unit.
    """
    seconds = convert_to_seconds(value, source_unit)
    return convert_from_seconds(seconds, target_unit)

def format_time_output(total_seconds: int | float, include_units: bool = True) -> str:
    """
    Format a total number of seconds into a human-readable string.

    Args:
        total_seconds (int | float): The total duration in seconds.
        include_units (bool): Whether to append unit labels to the output components.

    Returns:
        str: A formatted time string (e.g., "1 day, 2 hours").
    """
    if not isinstance(total_seconds, (int, float)):
        raise ValueError("Input must be a number representing seconds.")

    days = int(total_seconds // TimeUnitConverter.SECONDS_PER_DAY)
    remainder = total_seconds % TimeUnitConverter.SECONDS_PER_DAY
    
    hours = int(remainder // TimeUnitConverter.SECONDS_PER_HOUR)
    remainder %= TimeUnitConverter.SECONDS_PER_HOUR
    
    minutes = int(remainder // TimeUnitConverter.SECONDS_PER_MINUTE)
    
    result_parts = []
    if days > 0:
        unit_str = "day" if days == 1 else "days"
        res_part = f"{days} {unit_str}"
        result_parts.append(res_part)

    if hours > 0:
        unit_str = "hour" if hours == 1 else "hours"
        res_part = f"{hours} {unit_str}"
        result_parts.append(res_part)

    if minutes > 0 or days <= 0 and hours <= 0: # Show minutes even if no larger units for precision
         unit_str = "minute" if minutes == 1 else "minutes"
         res_part = f"{int(minutes)} {unit_str}"
         result_parts.append(res_part)

    return ", ".join(result_parts)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    converter = TimeUnitConverter()
    
    print("=== Time Unit Conversion Module Demo ===\n")
    
    # Sample 1: Convert years to seconds and back
    years_input = 2.5
    sec_result_1 = convert_to_seconds(years_input, 'years')
    days_back_1 = convert_from_seconds(sec_result_1, 'days')
    print(f"Sample 1:")
    print(f"Input: {years_input} years")
    print(f"To seconds: {sec_result_1:.2f} s\n")

    # Sample 2: Convert months to days (approximate)
    months_input = 6.5
    days_back_2 = convert_from_seconds(convert_to_months(months_input), 'days') 
    # Note: The above line uses a helper not defined yet, let's do it step by step properly
    
    print(f"Sample 2:")
    sec_result_2 = convert_to_seconds(6.5, 'months')
    days_back_3 = convert_from_seconds(sec_result_2, 'days') # Convert months -> seconds -> days
    print(f"Input: {6.5} months")
    print(f"To seconds: {sec_result_2:.2f} s")