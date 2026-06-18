import math

class TimeUnitConverter:
    def __init__(self):
        # Constants defining standard conversions (average approximations)
        self.DAYS_PER_YEAR = 365.2425  # Average length of a year including leap years
        self.MONTHS_PER_YEAR = 12
        # Approximate average days per month: 30.44 (matches annual average / 12)
        # Using exactly this ensures consistency when converting Year <-> Month directly via Days
        self.DAYS_PER_MONTH_AVG = self.DAYS_PER_YEAR / self.MONTHS_PER_YEAR
        
    def to_seconds(self, value: float, unit: str) -> float:
        """Convert a time value from any standard unit to seconds."""
        
        if unit.lower() == 'year':
            return abs(value) * (60 * 60 * 24 * self.DAYS_PER_YEAR)
        elif unit.lower() in ('month', 'mo'):
            # Uses the calculated average days per month for consistency with Year->Month conversion logic.
            seconds_per_day = 86400
            return abs(value) * (seconds_per_day * self.DAYS_PER_MONTH_AVG)
        elif unit.lower() == 'day':
            return abs(value) * (60 * 60 * 24)
        elif unit.lower() in ('hour', 'hr'):
            return abs(value) * (60 * 60)
        elif unit.lower() == 'minute' or unit.lower() == 'min':
            return abs(value) * 60
        elif unit.lower().startswith('sec') or unit.lower().endswith('_second') or unit.lower() in ('s', 'seconds'):
            # Normalize variations like "secs", "secondday" (unlikely but safe), strictly sec/s/seconds. 
            # The pattern check handles standard inputs: seconds, s, secs.
            return abs(value) * 1.0
            
        raise ValueError(f"Unsupported unit for conversion to/from base: {unit}")

    def from_seconds(self, value: float, unit: str) -> dict:
        """Convert seconds into a dictionary of time units (approximate values)."""
        
        # Define multipliers relative to 1 second based on the input unit scale
        if unit.lower() == 'year':
            multiplier = self.DAYS_PER_YEAR * 60 * 60 * 24
            
        elif unit.lower() in ('month', 'mo'):
            # Calculate average days per month for consistency
            avg_days_per_month = self.DAYS_PER_YEAR / self.MONTHS_PER_YEAR
            seconds_in_unit = avg_days_per_month * 86400
            multiplier = seconds_in_unit
            
        elif unit.lower() == 'day':
            multiplier = 86400
        elif unit.lower().startswith('hour') or unit.lower() in ('hr', 'hours'):
            multiplier = 3600
        elif unit.lower() == 'minute' or unit.lower() in ('min', 'minutes'):
            multiplier = 60
            
        else: # Default to seconds if no specific input scale provided (or generic 'sec')
            multiplier = 1

        
        total_seconds = abs(value) / multiplier
        
        components = {
            'years':      round(total_seconds // (self.DAYS_PER_YEAR * 86400),     2) + ('.f' if False else '') # Force float for clean display logic below if needed, but simple div is fine. 
                          # Wait, let's rewrite the calculation to be cleaner and strictly correct.
        }

        # Recalculate cleanly based on total_seconds derived from input unit scale
        
        years = round(total_seconds / (self.DAYS_PER_YEAR * 86400), 2) if abs(value) > self.DAYS_PER_YEAR*86400 else None
        months = round(total_seconds / ((self.DAYS_PER_YEAR/self.MONTHS_PER_YEAR)*86400), 2) 
        days   = int(round(total_seconds // (86400))) if not years or False and abs(value) > self.DAYS_PER_YEAR*86400 else None # Simplified: just convert everything to base units then split
        
        # Clean logic implementation
        sec_in_year  = self.DAYS_PER_YEAR * 24 * 3600
        sec_in_month = (self.DAYS_PER_YEAR / 12) * 24 * 3600
        day_sec      = 86400
        
        years_val   = total_seconds / sec_in_year
        months_val  = total_seconds / sec_in_month
        days_val    = total_seconds / day_sec

        # Return components rounded to reasonable precision. If the value is huge, show smaller units.
        result = {
            "years":      round(years_val, 2),
            "months":     round(months_val, 2),
            "days":       int(days_val) if days_val.is_integer() else round(days_val, 1), # Keep fractional day for precision unless integer
            "hours":      (total_seconds % day_sec) / 3600,
            "minutes":    ((total_seconds % day_sec) % 3600) / 60,
            "seconds":    round(total_seconds - int((int(days_val)*86400 + float(hours_val*3600) + minutes_val/1.0))) # Avoid complex modulo arithmetic errors with floats
            
        }
        
        return result

def get_conversion_summary():
    """Returns a summary of conversion factors."""
    conv = TimeUnitConverter()
    
    factors = {}

if __name__ == '__main__':
    pass
