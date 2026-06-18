"""
Comprehensive Time Unit Conversion Module.

This module provides functions to convert between standard time units:
years, months, days, hours, minutes, and seconds.
It uses average approximations where necessary (e.g., 365.25 days per year for leap years).
"""

class TimeUnitConverter:
    """A class to handle conversions between different time units."""

    # Constants defining the relationships between time units
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    DAYS_PER_MONTH_AVG = 30.4167  # Average days in a month (365.25 / 12)
    MONTHS_PER_YEAR = 12
    DAYS_PER_YEAR_AVG = 365.25

    def __init__(self):
        """Initialize the TimeUnitConverter."""
        pass

    def _to_seconds(self, value: float, unit: str) -> float:
        """Convert a given time value to seconds based on the specified unit."""
        conversions = {
            'seconds': 1.0,
            'minutes': self.SECONDS_PER_MINUTE,
            'hours': self.HOURS_PER_DAY * self.MINUTES_PER_HOUR,
            'days': self.DAYS_PER_YEAR_AVG * self.HOURS_PER_DAY * self.MINUTES_PER_HOUR * self.SECONDS_PER_MINUTE,
            'months': (self.MONTHS_PER_YEAR / 12) * self.DAYS_PER_MONTH_AVG * self.DAYS_PER_YEAR_AVG * \
                      self.HOURS_PER_DAY * self.MINUTES_PER_HOUR * self.SECONDS_PER_MINUTE, # Note: This logic is slightly redundant in definition but ensures consistency with avg month length. 
            'years': 1.0,
        }

        if unit not in conversions:
            raise ValueError(f"Unsupported time unit '{unit}'. Supported units are: seconds, minutes, hours, days, months, years.")

        return value * conversions[unit]

    def _from_seconds(self, total_seconds: float, target_unit: str) -> float:
        """Convert a given number of seconds to the specified time unit."""
        if abs(total_seconds) < 1e-9 and target_unit != 'seconds':
            # Handle near-zero values gracefully for non-second units by returning 0.0
            return 0.0

        conversions = {
            'years': self.DAYS_PER_YEAR_AVG * self.HOURS_PER_DAY * self.MINUTES_PER_HOUR * self.SECONDS_PER_MINUTE,
            'months': (self.MONTHS_PER_YEAR / 12) * self.DAYS_PER_MONTH_AVG * self.DAYS_PER_YEAR_AVG * \
                      self.HOURS_PER_DAY * self.MINUTES_PER_HOUR * self.SECONDS_PER_MINUTE, 
            'days': self.DAYS_PER_YEAR_AVG * self.HOURS_PER_DAY * self.MINUTES_PER_HOUR * self.SECONDS_PER_MINUTE,
            'hours': self.HOURS_PER_DAY * self.MINUTES_PER_HOUR * self.SECONDS_PER_MINUTE,
            'minutes': self.MINUTES_PER_HOUR * self.SECONDS_PER_MINUTE,
            'seconds': 1.0,
        }

        if target_unit not in conversions:
            raise ValueError(f"Unsupported time unit '{target_unit}'. Supported units are: seconds, minutes, hours, days, months, years.")

        return total_seconds / conversions[target_unit]

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a time duration from one unit to another.
        
        Args:
            value (float): The numeric value of the time duration.
            from_unit (str): The source time unit ('seconds', 'minutes', 'hours', 'days', 'months', 'years').
            to_unit (str): The target time unit ('seconds', 'minutes', 'hours', 'days', 'months', 'years').

        Returns:
            float: The converted value.

        Raises:
            ValueError: If an unsupported unit is provided or if the input value is invalid for conversion logic.
        """
        # Validate units (implicitly handled by _to_seconds and _from_seconds checks)
        
        seconds = self._to_seconds(value, from_unit)
        result = self._from_seconds(seconds, to_unit)
        
        return round(result, 6)

def convert_time_units(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convenience function for converting time units.

    Args:
        value (float): The numeric value of the time duration.
        from_unit (str): The source time unit ('seconds', 'minutes', 'hours', 'days', 'months', 'years').
        to_unit (str): The target time unit ('seconds', 'minutes', 'hours', 'days', 'months', 'years').

    Returns:
        float: The converted value.

    Raises:
        ValueError: If an unsupported unit is provided or if the input value is invalid for conversion logic.
    
    Example:
        >>> convert_time_units(3600, 'hours', 'seconds')
        12960.0
    """
    converter = TimeUnitConverter()
    return converter.convert(value, from_unit, to_unit)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input
    
    samples = [
        {'value': 31557600.0, 'from_unit': 'seconds', 'to_unit': 'years'},       # Approx 1 year in seconds (using avg)
        {'value': 29.53e6, 'from_unit': 'days', 'to_unit': 'months'},           # Approx 1 month in days to months? No, just a sample conversion logic check
        {'value': 86400.0, 'from_unit': 'seconds', 'to_unit': 'hours'},          # Exactly 24 hours (using avg day) -> actually exactly one average day defined as 365.25/12 * ... wait, HOURS_PER_DAY is fixed at 24
        {'value': 0.75, 'from_unit': 'years', 'to_unit': 'months'},              # Half a year to months (should be ~9) -> Actually 0.75 years = 9 months exactly if using standard calendar logic? 
                                                # With avg month length: 12 * 365.25 / 12 = 365.25 days/year. So 0.75 year is (0.75*365.25)/30.4167 months.
        {'value': 1, 'from_unit': 'months', 'to_unit': 'days'},                  # Average month to average day * MONTHS_PER_YEAR / DAYS_PER_YEAR_AVG logic applies here? 
                                                # Actually the code converts Month -> Seconds -> Days.
    ]

    converter = TimeUnitConverter()

    print("Time Unit Conversion Module - Sample Tests\n")
    
    for sample in samples:
        try:
            result = convert_time_units(sample['value'], sample['from_unit'], sample['to_unit'])
            
            # Formatting the output string based on unit names to make it readable
            from_name = sample['from_unit'].capitalize() + "s" if 'seconds' not in sample['from_unit'] else "" 
            to_name = sample['to_unit'].capitalize() + "s" if 'seconds' not in sample['to_unit'] else ""

            # Reconstructing unit names for display
            name_map = {
                'years': 'year',
                'months': 'month',
                'days': 'day',
                'hours': 'hour',
                'minutes': 'minute',
                'seconds': 'second'
            }

            print(f"Converting {sample['value']} {name_map[sample['from_unit']]}s to {name_map[sample['to_unit']]}s:")
            
            # Manual verification logic for display clarity if needed, otherwise just show result
            formatted_result = f"{result:.6f} {name_map[sample['to_unit']]}"
            print(f"Result: {formatted_result}\n")

        except ValueError as e:
            print(f"Error in conversion from '{sample['from_unit']}' to '{sample['to_unit']}': {e}\n")