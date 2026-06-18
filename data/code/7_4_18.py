"""
Comprehensive Time Unit Conversion Module.

This module provides functions to convert between standard time units:
years, months, days, hours, minutes, and seconds.

Assumptions made for approximations:
- 1 year = 365.2425 days (Gregorian calendar average)
- 1 month = 30.4375 days (average length of a month in the Gregorian calendar)
- 1 day = 24 hours
- 1 hour = 60 minutes
- 1 minute = 60 seconds

All conversion functions handle both directions: from larger to smaller units 
and vice-versa. Negative values are supported and will result in negative outputs,
representing time durations (e.g., -5 years).
"""

class TimeUnitConverter:
    """A class for converting between different standard time units."""

    # Constants defining the relationships between units
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    DAYS_PER_YEAR_AVERAGE = 365.2425
    DAYS_PER_MONTH_AVERAGE = 30.4375

    # Unit names for mapping purposes (lowercase)
    UNITS = {
        'seconds': 1,
        'minutes': SECONDS_PER_MINUTE,
        'hours': HOURS_PER_DAY * MINUTES_PER_HOUR,
        'days': DAYS_PER_YEAR_AVERAGE * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE,
        'months': DAYS_PER_MONTH_AVERAGE * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE,
        'years': 365.2425 * DAYS_PER_MONTH_AVERAGE * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE,
    }

    def __init__(self):
        """Initialize the converter with standard constants."""
        pass

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a time duration from one unit to another.

        Args:
            value (float): The numerical value of the time duration in 'from_unit'.
            from_unit (str): The source unit ('years', 'months', 'days', 'hours', 
                             'minutes', or 'seconds'). Must be lowercase.
            to_unit (str): The target unit. Must be lowercase.

        Returns:
            float: The converted value in the 'to_unit'.

        Raises:
            ValueError: If an invalid unit is provided.
        """
        if from_unit not in self.UNITS or to_unit not in self.UNITS:
            raise ValueError(f"Invalid time units. Supported units are: {list(self.UNITS.keys())}")

        # Convert value to seconds first (the base unit)
        source_factor = self.UNITS[from_unit]
        target_factor = self.UNITS[to_unit]

        if from_unit == 'seconds':
            converted_seconds = value * 1.0
        else:
            # For all other units, divide by the factor to get seconds (since factors > 1)
            # Actually, let's think about it differently for clarity:
            # Value in source unit -> Seconds -> Value in target unit
            
            # If we have X years, how many seconds? 
            # value * (seconds per year) = total_seconds
            converted_seconds = value * source_factor

        if to_unit == 'seconds':
            return converted_seconds / 1.0
        
        else:
            # Convert seconds back to target unit
            return converted_seconds / target_factor

def convert_time(value, from_unit, to_unit):
    """
    Convenience function for converting time units using the TimeUnitConverter class.

    Args:
        value (float): The numerical value of the time duration in 'from_unit'.
        from_unit (str): The source unit ('years', 'months', 'days', 'hours', 
                         'minutes', or 'seconds'). Must be lowercase.
        to_unit (str): The target unit. Must be lowercase.

    Returns:
        float: The converted value in the 'to_unit'.

    Raises:
        ValueError: If an invalid unit is provided.
    """
    converter = TimeUnitConverter()
    return converter.convert(value, from_unit, to_unit)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input
    
    samples = [
        {
            'value': 10, 
            'from_unit': 'years', 
            'to_unit': 'seconds'
        },
        {
            'value': -5.5, 
            'from_unit': 'months', 
            'to_unit': 'days'
        },
        {
            'value': 3600, 
            'from_unit': 'hours', 
            'to_unit': 'minutes'
        },
        {
            'value': 12.5, 
            'from_unit': 'seconds', 
            'to_unit': 'years'
        }
    ]

    print("Time Unit Conversion Results")
    print("=" * 40)

    for sample in samples:
        value = sample['value']
        from_u = sample['from_unit']
        to_u = sample['to_unit']

        try:
            result = convert_time(value, from_u, to_u)
            
            # Format output nicely based on magnitude if needed, 
            # but keeping it simple as per request constraints.
            print(f"Converting {value} {from_u}")
            print(f"to {result:.6f} {to_u}\n")

        except ValueError as e:
            print(f"Error converting from '{from_u}' to '{to_u}': {e}\n")