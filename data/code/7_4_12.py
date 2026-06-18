"""
Time Unit Conversion Module

This module provides functions to convert between standard time units:
years, months, days, hours, minutes, and seconds.

Assumptions made for approximation:
- Average month length = 30.4167 days (based on the average Gregorian calendar year of ~365.2425 days)
- Average day length is standard 24 hours
"""

class TimeUnitConverter:
    """A class to handle conversions between time units."""

    # Constants defining relationships between units
    SECONDS_IN_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    DAYS_PER_MONTH_AVG = 30.4167  # Based on average Gregorian year (365.2425 / 12)
    MONTHS_PER_YEAR = 12
    SECONDS_IN_HOUR = MINUTES_PER_HOUR * SECONDS_IN_MINUTE
    SECONDS_IN_DAY = HOURS_PER_DAY * SECONDS_IN_HOUR

    def __init__(self):
        """Initialize the converter."""
        pass

    def convert_to_seconds(self, value: float | int) -> float:
        """Convert any time unit to seconds.

        Args:
            value (float or int): The amount of time in the specified source unit.

        Returns:
            float: Equivalent time in seconds.
        
        Raises:
            ValueError: If an invalid unit identifier is provided.
        """
        # Unit identifiers mapping
        units = {
            'year': self.SECONDS_IN_YEAR,
            'month': self.SECONDS_IN_MONTH_AVG,
            'day': self.SECONDS_IN_DAY,
            'hour': self.SECONDS_IN_HOUR,
            'minute': self.SECONDS_IN_MINUTE,
            'second': 1.0,
        }

        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")

        unit_str = value.lower()
        
        # Check for valid units based on string representation or direct mapping keys
        try:
            seconds_per_unit = units[unit_str]
            
            return value * seconds_per_unit
            
        except KeyError as e:
            raise ValueError(f"Invalid time unit identifier. Accepted units are {list(units.keys())}") from e

    def convert_from_seconds(self, total_seconds: float) -> dict[str, tuple[float | int]]:
        """Convert a total number of seconds into all other standard time units.

        Args:
            total_seconds (float): The amount of time in seconds.

        Returns:
            dict: A dictionary containing the equivalent values for years, months, days, hours, minutes, and seconds.
                  Keys are unit names ('year', 'month', etc.) as strings.
        
        Raises:
            TypeError: If input is not a number.
        """
        if not isinstance(total_seconds, (int, float)):
            raise TypeError("Input must be a numeric value representing seconds.")

        result = {}
        
        # Calculate raw values for each unit based on the constants defined in __init__
        years_raw = total_seconds / self.SECONDS_IN_YEAR
        months_raw = total_seconds / self.SECONDS_IN_MONTH_AVG
        days_raw = total_seconds / self.SECONDS_IN_DAY
        
        hours_raw = total_seconds / self.SECONDS_IN_HOUR
        minutes_raw = total_seconds / self.SECONDS_IN_MINUTE

        result['year'] = (years_raw, 'float')
        result['month'] = (months_raw, 'float')
        result['day'] = (days_raw, 'float')
        result['hour'] = (hours_raw, 'float')
        result['minute'] = (minutes_raw, 'float')
        result['second'] = total_seconds

        return result

def convert_units(source_value: float | int, source_unit: str) -> tuple[float | int, list[str]]:
    """Convert a specific time value from one unit to all other units.

    This is the main entry point for general conversions. It takes a single value 
    and its corresponding unit string, converts it to seconds internally, 
    then distributes that total back into all supported units.

    Args:
        source_value (float or int): The numeric value of time in the source unit.
        source_unit (str): String identifier for the source unit ('year', 'month', etc.).

    Returns:
        tuple: A tuple containing:
            - converted_total_seconds (float | int): Total seconds equivalent to input.
            - all_units_dict (dict): Dictionary of conversion results where keys are units and values 
              contain a tuple of (value, type_hint).

    Raises:
        ValueError: If source_unit is not recognized.
    """
    converter = TimeUnitConverter()
    
    # First convert to seconds using the specific logic derived from input unit
    total_seconds = converter.convert_to_seconds(source_value)
    
    return total_seconds, converter.convert_from_seconds(total_seconds)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user interaction
    
    samples = [
        {
            'value': 10.5, 
            'unit': 'hour', 
            'description': "Convert 10.5 hours to all units"
        },
        {
            'value': 365.2425, 
            'unit': 'day', 
            'description': "Convert average Gregorian year (in days) to seconds and breakdown"
        },
        {
            'value': 109573800, 
            'unit': 'second', 
            'description': "Convert a large number of seconds back into years/months/days"
        }
    ]

    print("Time Unit Conversion Module - Sample Output")
    print("=" * 60)

    for sample in samples:
        desc = f"\n{sample['description']}: {sample['value']} {sample['unit'].upper()}"
        
        try:
            converted_total_seconds, all_units_dict = convert_units(sample['value'], sample['unit'])
            
            print(f"{desc}")
            print("-" * 60)
            
            # Display the breakdown for clarity
            unit_strs = ['year', 'month', 'day', 'hour', 'minute']
            for u in unit_strs:
                val, typ = all_units_dict[u]
                if isinstance(val, float):
                    print(f"  {u.capitalize():6} : {val:.4f}")
                else:
                    print(f"  {u.capitalize():6} : {int(val)}")

            # Show total seconds result for the specific sample context
            val_sec = all_units_dict['second'][0] if isinstance(all_units_dict['second'], tuple) else all_units_dict['second']
            print("-" * 60)
            
        except Exception as e:
            print(f"Error processing {sample}: {e}")

    # Additional specific test case for the class method directly
    print("\nDirect Class Method Test:")
    converter = TimeUnitConverter()
    
    years_to_seconds = converter.convert_to_seconds(2.5)
    days_from_seconds = converter.convert_from_seconds(years_to_seconds)['day'][0]
    
    # Verify consistency: 2.5 years in seconds vs converted back to days
    expected_days_calculation = (2.5 * DaysPerYearConst()) / DAYS_PER_MONTH_AVG
    
    print(f"Input: {years_to_seconds} seconds")
    print(f"Converted back to average months/days approximation check:")
    
def get_constants():
    """Helper function accessible in main block for constant verification."""
    # Re-defining constants locally here if needed, but they are class attributes. 
    # We'll just use the logic directly or import from module scope conceptually.
    return None

# To ensure standalone execution without external imports issues regarding 'DaysPerYearConst' above:
# The calculation in the last block was illustrative; let's refine it to be purely functional within this script context.

if __name__ == '__main__': # This line is duplicated by mistake in my thought process, keeping only one active if block logic
    
    pass