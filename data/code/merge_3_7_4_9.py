"""
Comprehensive Time Unit Conversion Module.

This module provides functions to convert between standard time units:
years, months, days, hours, minutes, and seconds.

Assumptions made for average approximations where exact calendar definitions vary:
- 1 year = 365.25 days (accounting for leap years on average)
- 1 month = 30.4167 days (average of months in a Gregorian year, or simply 365.25 / 12)
- 1 day = 24 hours
- 1 hour = 60 minutes
- 1 minute = 60 seconds

All conversion functions handle both positive and negative values correctly for durations.
"""

class TimeUnitConverter:
    """A class to convert between different time units."""

    # Define constants based on average approximations
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    DAYS_PER_YEAR = 365.25
    MONTHS_PER_YEAR = 12
    
    def __init__(self):
        """Initialize the converter with standard constants."""
        pass

    @staticmethod
    def _get_seconds(value, unit_from):
        """Convert a value from 'unit_from' to seconds internally for processing."""
        if unit_from == "years":
            return value * TimeUnitConverter.DAYS_PER_YEAR * TimeUnitConverter.HOURS_PER_DAY \
                   * TimeUnitConverter.MINUTES_PER_HOUR * TimeUnitConverter.SECONDS_PER_MINUTE
        elif unit_from == "months":
            # Using average month length: 365.25 / 12 days per month
            return value * (TimeUnitConverter.DAYS_PER_YEAR / TimeUnitConverter.MONTHS_PER_YEAR) \
                   * TimeUnitConverter.HOURS_PER_DAY * TimeUnitConverter.MINUTES_PER_HOUR \
                   * TimeUnitConverter.SECONDS_PER_MINUTE
        elif unit_from == "days":
            return value * TimeUnitConverter.HOURS_PER_DAY * TimeUnitConverter.MINUTES_PER_HOUR \
                   * TimeUnitConverter.SECONDS_PER_MINUTE
        elif unit_from == "hours":
            return value * TimeUnitConverter.MINUTES_PER_HOUR * TimeUnitConverter.SECONDS_PER_MINUTE
        elif unit_from == "minutes":
            return value * TimeUnitConverter.SECONDS_PER_MINUTE
        elif unit_from == "seconds":
            return value
        else:
            raise ValueError(f"Unsupported time unit for conversion from: {unit_from}")

    @staticmethod
    def _get_multiplier(unit_to, seconds_per_unit):
        """Calculate the multiplier to convert back from seconds to a specific target unit."""
        if unit_to == "years":
            return 1.0 / (TimeUnitConverter.DAYS_PER_YEAR * TimeUnitConverter.HOURS_PER_DAY \
                          * TimeUnitConverter.MINUTES_PER_HOUR * TimeUnitConverter.SECONDS_PER_MINUTE)
        elif unit_to == "months":
            # Average month length in seconds: (365.25/12) * 86400
            return 1.0 / ((TimeUnitConverter.DAYS_PER_YEAR / TimeUnitConverter.MONTHS_PER_YEAR) \
                          * TimeUnitConverter.HOURS_PER_DAY * TimeUnitConverter.MINUTES_PER_HOUR \
                          * TimeUnitConverter.SECONDS_PER_MINUTE)
        elif unit_to == "days":
            return 1.0 / (TimeUnitConverter.HOURS_PER_DAY * TimeUnitConverter.MINUTES_PER_HOUR \
                         * TimeUnitConverter.SECONDS_PER_MINUTE)
        elif unit_to == "hours":
            return 1.0 / (TimeUnitConverter.MINUTES_PER_HOUR * TimeUnitConverter.SECONDS_PER_MINUTE)
        elif unit_to == "minutes":
            return 1.0 / TimeUnitConverter.SECONDS_PER_MINUTE
        elif unit_to == "seconds":
            return 1.0
        else:
            raise ValueError(f"Unsupported time unit for conversion to: {unit_to}")

    def convert(self, value, from_unit, to_unit):
        """
        Convert a duration from one time unit to another.

        Args:
            value (float or int): The magnitude of the time duration.
            from_unit (str): Source unit ('years', 'months', 'days', 'hours', 'minutes', 'seconds').
            to_unit (str): Target unit ('years', 'months', 'days', 'hours', 'minutes', 'seconds').

        Returns:
            float: The converted value.

        Raises:
            ValueError: If the input units are not recognized or if value is invalid.
        """
        valid_units = ["years", "months", "days", "hours", "minutes", "seconds"]
        
        if from_unit not in valid_units:
            raise ValueError(f"Invalid source unit '{from_unit}'. Valid options: {', '.join(valid_units)}")
        if to_unit not in valid_units:
            raise ValueError(f"Invalid target unit '{to_unit}'. Valid options: {', '.join(valid_units)}")

        # Handle zero value directly
        if abs(value) < 1e-9:
            return 0.0

        try:
            seconds = self._get_seconds(float(value), from_unit)
            result = float(seconds * self._get_multiplier(to_unit, None))
            
            # Clean up floating point errors (e.g., 24 hours to days should be exactly 1.0 or close enough)
            if abs(result - round(result, 6)) < 1e-9:
                return round(result, 5)
            else:
                return result
                
        except ValueError as e:
            raise ValueError(f"Invalid input value for time conversion: {value}") from e

def convert_time(value, unit_from, unit_to):
    """
    Convenience function to convert between time units.

    Args:
        value (float or int): The magnitude of the time duration.
        unit_from (str): Source unit ('years', 'months', 'days', 'hours', 'minutes', 'seconds').
        unit_to (str): Target unit ('years', 'months', 'days', 'hours', 'minutes', 'seconds').

    Returns:
        float: The converted value.
    
    Raises:
        ValueError: If the input units are not recognized or if value is invalid.
    """
    converter = TimeUnitConverter()
    return converter.convert(value, unit_from, unit_to)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    print("Time Unit Conversion Module Demo")
    print("-" * 30)