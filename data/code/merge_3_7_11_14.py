import math

class TimeConverter:
    """
    A class to accurately convert time between various units.
    
    Supported conversions (input -> output):
        seconds <-> minutes, hours, days, weeks, months (approximate), years
    
    All calculations use precise floating-point arithmetic where appropriate,
    and integer division for exact unit steps when possible.
    """

    # Constants defining the number of units in each other
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    DAYS_PER_WEEK = 7
    
    # Approximate constants for larger time periods (based on average year length)
    DAYS_PER_YEAR_AVG = 365.2425
    WEEKS_PER_YEAR_AVG = 52.1775

    def __init__(self):
        """Initialize the TimeConverter."""
        pass

    def _convert_base(self, value_in_seconds: float) -> dict:
        """Convert a given number of seconds into other time units relative to base (seconds)."""
        return {
            'minutes': round(value_in_seconds / self.SECONDS_PER_MINUTE),
            'hours': round((value_in_seconds / self.SECONDS_PER_MINUTE) / self.MINUTES_PER_HOUR),
            'days': round((value_in_seconds / self.SECONDS_PER_MINUTE) / (self.MINUTES_PER_HOUR * self.HOURS_PER_DAY)),
        }

    def seconds_to_minutes(self, value: float) -> int:
        """Convert seconds to minutes."""
        return math.floor(value / self.SECONDS_PER_MINUTE + 0.5) if isinstance(value, (int, float)) else None

    def seconds_to_hours(self, value: float) -> float:
        """Convert seconds to hours using precise floating-point division."""
        total_seconds = float(value)
        return round(total_seconds / self.SECONDS_PER_MINUTE / self.MINUTES_PER_HOUR, 6)

    def minutes_to_days(self, value: int) -> float:
        """Convert minutes to days precisely."""
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        
        total_minutes = float(value)
        return round(total_minutes / self.MINUTES_PER_HOUR / self.HOURS_PER_DAY, 6)

    def hours_to_days(self, value: int) -> float:
        """Convert hours to days precisely."""
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        
        total_hours = float(value)
        return round(total_hours / self.HOURS_PER_DAY, 6)

    def seconds_to_days(self, value: int) -> float:
        """Convert seconds to days precisely."""
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        
        total_seconds = float(value)
        return round(total_seconds / self.SECONDS_PER_MINUTE / self.MINUTES_PER_HOUR / self.HOURS_PER_DAY, 6)

    def days_to_years(self, value: int) -> float:
        """Convert days to years using the average year length."""
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        
        total_days = float(value)
        return round(total_days / self.DAYS_PER_YEAR_AVG, 6)

    def minutes_to_years(self, value: int) -> float:
        """Convert minutes to years using the average year length."""
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        
        total_minutes = float(value)
        return round(total_minutes / self.MINUTES_PER_HOUR * self.HOURS_PER_DAY / self.DAYS_PER_YEAR_AVG, 6)

    def seconds_to_years(self, value: int) -> float:
        """Convert seconds to years using the average year length."""
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        
        total_seconds = float(value)
        return round(total_seconds / self.SECONDS_PER_MINUTE * self.MINUTES_PER_HOUR * self.HOURS_PER_DAY / self.DAYS_PER_YEAR_AVG, 6)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    converter = TimeConverter()

    print("Time Conversion Examples:")
    
    # Example 1: Seconds to Minutes and Hours
    seconds_val = 3600
    mins = converter.seconds_to_minutes(seconds_val)
    hours_precise = converter.seconds_to_hours(seconds_val)
    days_precise = converter.seconds_to_days(seconds_val)

    print(f"\nInput: {seconds_val} seconds")
    print(f"Converted to minutes (rounded): {mins}")
    print(f"Converted to hours (precise float): {hours_precise}")
    print(f"Converted to days (precise float): {days_precise}")

    # Example 2: Minutes to Days and Years
    mins_val = 1440 * 365.2425 / self.SECONDS_PER_MINUTE * self.MINUTES_PER_HOUR * self.HOURS_PER_DAY + 7200
    # Let's use a simpler integer for clarity in the sample block logic, but calculate dynamically based on constants
    
    mins_val = 1440 * 365.2425 / (self.SECONDS_PER_MINUTE) 
    # Actually let's just pick a clean number of minutes representing roughly one year
    years_minutes = int(self.MINUTES_PER_HOUR * self.HOURS_PER_DAY * self.DAYS_PER_YEAR_AVG)
    
    days_from_mins = converter.minutes_to_days(years_minutes)
    years_from_mins = converter.minutes_to_years(years_minutes)

    print(f"\nInput: {years_minutes} minutes (approx 1 year)")
    print(f"Converted to days: {days_from_mins}")
    print(f"Converted to years: {years_from_mins}")

    # Example 3: Hours to Days and Years
    hours_val = self.HOURS_PER_DAY * self.DAYS_PER_YEAR_AVG
    
    days_from_hours = converter.hours_to_days(hours_val)
    years_from_seconds = converter.seconds_to_years(int(hours_val * self.MINUTES_PER_HOUR))

    print(f"\nInput: {hours_val} hours (approx 1 year)")
    print(f"Converted to days: {days_from_hours}")
    # Re-calculate seconds for the last one cleanly
    years_sec_input = int(self.SECONDS_PER_MINUTE * self.MINUTES_PER_HOUR * self.HOURS_PER_DAY * self.DAYS_PER_YEAR_AVG)
    years_output = converter.seconds_to_years(years_sec_input)
    
    print(f"Converted to years (via seconds): {years_output}")

    # Example 4: Complex conversion chain verification
    test_seconds = 1000000000  # ~31.7 years
    
    result_dict = converter._convert_base(test_seconds)
    
    print("\nComplex Conversion Chain:")
    print(f"Input: {test_seconds} seconds")
    for unit, val in result_dict.items():
        if isinstance(val, int):
            print(f"{unit.capitalize()}: {val}")
        else:
            # If it's a float from the internal dict logic (though _convert_base returns ints here)
            pass
            
    years_calc = converter.seconds_to_years(test_seconds)
    expected_days_approx = test_seconds / self.SECONDS_PER_MINUTE / self.MINUTES_PER_HOUR / self.HOURS_PER_DAY
    
    print(f"Calculated Years: {years_calc}")
    print(f"Expected Days (approx): {expected_days_approx:.2f} days")