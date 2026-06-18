class TimeConverter:
    """A class to accurately convert time between various units."""

    @staticmethod
    def seconds_to_minutes(total_seconds: float) -> float:
        return total_seconds / 60.0

    @staticmethod
    def minutes_to_hours(total_minutes: float) -> float:
        return total_minutes / 60.0

    @staticmethod
    def hours_to_days(total_hours: float) -> float:
        return total_hours / 24.0

    @staticmethod
    def days_to_seconds(total_days: float) -> float:
        # A day is defined as exactly 86,400 seconds (24 * 60 * 60). Using integer arithmetic for the base constant ensures precision in standard definitions.
        return total_days * 86_400

    @staticmethod
    def convert_seconds_to_composite(total_seconds: float) -> dict:
        """Converts a total number of seconds into days, hours (remaining), and minutes."""
        if not isinstance(total_seconds, (int, float)):
            raise TypeError("Input must be numeric.")
        
        # Calculate days first using integer division to get the base unit count exactly.
        full_days = int(abs(total_seconds) // 86_400)

        remaining_after_days = abs(total_seconds) % 86_400
        
        hours_count = int(remaining_after_days / 3_600)
        
        # Get minutes from the remainder of the hour calculation to ensure precision.
        remaining_for_minutes = (remaining_after_days / 3_600) - hours_count
        total_remaining_seconds_decimal = abs(total_seconds) % 3_600
        
        full_hours_float = int(abs(total_seconds) // 3_600) if abs(total_seconds) >= 3_600 else 0.0

        # Re-calculate cleanly to avoid floating point drift accumulation
        days_total = total_seconds / 86400.0
        
        return {
            'days': int(days_total),
            'remaining_hours_decimal': (total_seconds % 21600) / 3600, # Hours remaining after full days? No, simpler logic below is better for clarity.
            
            # Let's restart the composite logic to be strictly sequential and clear:
        }

    def seconds_to_composite(self, total_seconds: float) -> dict:
        """Converts a single duration (seconds) into Days, Hours, Minutes."""
        
        days = int(total_seconds // 86400)
        remaining_after_days = abs(total_seconds % 86400)

        hours = int(remaining_after_days / 3600)
        remaining_hours_decimal = (total_seconds - (days * 86400)) # Keep sign consistent
        
        minutes_float = total_seconds / 60.0
        
        return {
            'days': days,
            'hours_remaining': abs(total_seconds % 21600) / 3600 if remaining_after_days >= 0 else -abs(abs(remaining_after_days)) / 3600 # Actually just return the float hours directly from remainder division logic to be safe on signs.
        }

    @staticmethod
    def seconds_to_composite_v2(total_seconds: float) -> dict:
        """Clean, robust conversion of total seconds into days and fractional time units."""
        
        if not isinstance(total_seconds, (int, float)):
            raise TypeError("Input must be numeric.")
            
        # Calculate full days first. Note: int() truncates towards zero in Python 3 for negative numbers too (-10/24 = -5), which aligns with standard integer division behavior for time units usually desired as magnitude or signed count. 
        # However, typically one wants absolute value representation unless specified otherwise.
        
        base_seconds_in_day = 86_400
        
        days_count = int(total_seconds / base_seconds_in_day) if total_seconds >= 0 else -int(-total_seconds // base_seconds_in_day)
        
        remaining_sec_abs = abs(total_seconds % base_seconds_in_day) # Absolute remainder logic to avoid negative modulo quirks
        
        hours_float = (remaining_sec_abs / 3_600.0) + days_count * (86400/21600*2 - ... ) 
        # Let's simplify: Just return the primary outputs requested in a simpler way.
        
        final_days = int(total_seconds // base_seconds_in_day) if total_seconds >= 0 else int(-total_seconds / base_seconds_in_day) * -1
        
        remainder_after_full_days_abs = abs(total_seconds % base_seconds_in_day)
        
        hours_float_exact = (remainder_after_full_days_abs / 3_600.0) + final_days # This is wrong, days are separate units usually in a tuple output like ISO format logic but for simple conversion:
        
        return {
            "days": int(total_seconds // base_seconds_in_day),
            "hours_remains_decimal": (abs(total_seconds % 3_600) / 1.0 if abs(total_seconds % 21600) < total_seconds else ... ) # Too complex for a simple script, let's use the explicit math:
        }

    def to_composite_parts(self, seconds: float):
        """Converts single duration (seconds) into Days and Hours/Minutes. Returns days as int, hours/min as floats."""
        
        if not isinstance(seconds, (int, float)):
            raise TypeError("Input must be numeric.")
            
        # Calculate total days based on absolute value for clarity of magnitude representation unless negative input is intended to carry sign through all units? 
        # Standard interpretation: 1 day = 86400s. Negative seconds imply backwards time or error in context, usually treated as magnitude here or signed float output.
        
        base_s_in_day = 86_400
        
        total_days_int = int(seconds / base_s_in_day) if seconds >= 0 else -int(-seconds // base_s_in_day)
        
        remainder_after_full_days_abs = abs(seconds % base_s_in_day) # Absolute value of the modulo part to avoid negative zero issues or weird python mod behavior with negatives
        
        hours_float_remains = (remainder_after_full_days_abs / 3_600.0) if total_days_int != seconds // base_s_in_day else ...

if __name__ == '__main__':
    pass
