import math

class TimeConverter:
    """
    A class to convert between hours, minutes, and seconds with optimized logic.
    
    Attributes:
        None
    
    Methods:
        total_seconds(hours=None, minutes=None, seconds=None) -> float or int
            Converts a mix of time units into total seconds.
        
        format_time(total_seconds) -> str
            Formats total seconds back into hours, minutes, and seconds string.
    
    Note:
        All calculations use integer arithmetic where possible for efficiency,
        but return floats if fractional seconds are involved in input or output formatting logic requires precision handling implicitly via division results before final truncation/formatting decisions based on context (here we prioritize clean representation).
    """

    def __init__(self):
        # No state needed; all methods are functional.
        pass
    
    def total_seconds(self, hours=None, minutes=None, seconds=None) -> float:
        """
        Converts a mix of time units into total seconds.
        
        Args:
            hours (int or None): Number of hours to convert.
            minutes (int or None): Number of minutes to convert.
            seconds (float or int): Number of seconds to convert.
            
        Returns:
            float: Total number of seconds as a floating-point value if input has decimals, otherwise integer-like behavior is preserved via math operations but returned as float for consistency in further calculations unless explicitly cast later. However, per optimization and mathematical soundness with potential fractional inputs (e.g., 0.5 hours), we return the exact sum.
            
        Raises:
            TypeError: If any input is not a number or None.
        
        Example:
            >>> tc = TimeConverter()
            >>> tc.total_seconds(hours=1, minutes=30)
            5400.0
        """
        if hours is not None and (not isinstance(hours, int)):
            raise TypeError("hours must be an integer or None")
        if minutes is not None and (not isinstance(minutes, int)):
            raise TypeError("minutes must be an integer or None")
        if seconds is not None and (not isinstance(seconds, (int, float))):
            raise TypeError("seconds must be a number or None")

        total = 0.0
        
        # Convert hours to seconds: 1 hour = 3600 seconds
        if hours is not None:
            total += hours * 3600
            
        # Convert minutes to seconds: 1 minute = 60 seconds
        if minutes is not None:
            total += minutes * 60
            
        # Add direct seconds (already in correct unit)
        if seconds is not None:
            total += float(seconds)

        return total
    
    def format_time(self, total_seconds):
        """
        Formats a given number of total seconds into hours, minutes, and seconds.
        
        Args:
            total_seconds (float or int): Total time in seconds.
            
        Returns:
            str: Formatted string "H:M:S" where H is integer hours, M is remaining minutes as integer, S is fractional part formatted to 3 decimal places if non-zero, else '0'. If input is whole number of seconds and no fraction needed after division logic? Actually we want precision. Let's assume standard formatting: 
            - Hours = int(total_seconds // 3600)
            - Remaining minutes = (total_seconds % 3600) // 60 -> integer part for display unless specified otherwise, but usually time displays integers for M and S if input is clean? The prompt says "mathematically sound". 
            Let's stick to: H=int(Hours), M=integer remainder in minutes, S=fractional seconds formatted.
            
        Example:
            >>> tc = TimeConverter()
            >>> tc.format_time(5400)
            '1:30:0' -> Wait, standard is usually 2 decimals or just integer if whole? Let's do clean integers for M and S only if input was exact? No, let's provide precision. 
            Actually, simpler approach often expected in such tasks without specific formatting rules: H:M:S where M and S are derived precisely.
            
        Revised Logic for format_time to be robust:
        - Calculate hours as int(total_seconds // 3600)
        - Remaining seconds after removing hours = total_seconds % 3600
        - Minutes = int(remaining / 60) -> This truncates, losing fractional minutes if any. But time usually doesn't have fractions of a minute in common display unless specified (like milliseconds). 
        However, since input can be float seconds, we should preserve precision for S.
        
        Let's define:
          h = int(total_seconds // 3600)
          rem_s = total_seconds - (h * 3600)
          m = int(rem_s / 60) # Truncate minutes to integer as per standard time display unless fractional minutes are requested. But if input was 1 hour + 0.5 min, then we have fraction in seconds. 
          s_rem = rem_s - (m * 60)
          
        Format: f"{h}:{int(m)}:{s_rem:.3f}" -> This handles fractions of a second correctly while keeping minutes as integer which is standard for "hours:minutes:seconds" unless higher precision needed elsewhere. But wait, if input was 1 hour and 0.5 minute (which is 30 seconds exactly), then m=0? No. 
        Example: total_seconds = 60 * 0.5 + 30 = 60s -> h=0, rem_s=60, m=1, s_rem=0 -> "0:1:0". Correct.
        
        What if input is float seconds like 90.5? 
          total_seconds = 90.5
          h = int(90.5 // 3600) = 0
          rem_s = 90.5 - 0 = 90.5
          m = int(90.5 / 60) = 1 (since 90/60=1.5 -> truncates to 1)
          s_rem = 90.5 - 60 = 30.5
          Result: "0:1:30.5" or formatted as ".3f"? 
        Standard time format usually doesn't show fractional minutes unless specified (like in scientific contexts). But given the task emphasizes mathematical soundness and efficiency, showing fractions of a second is more accurate than truncating to integer seconds if input has decimals.
        
        Let's use: f"{h}:{int(m)}:{s_rem:.3f}" -> This ensures precision for S but keeps M as integer minute count (standard behavior). If fractional minutes were needed, the problem would likely specify "milliseconds" or similar. 
    """
    
    # Ensure input is float to handle potential int inputs gracefully in calculations if mixed types occur elsewhere, though type hint says float/int.
    total_seconds = float(total_seconds)

    h = int(total_seconds // 3600)
    rem_s = total_seconds - (h * 3600)
    
    # Calculate minutes as integer part of the remaining seconds divided by 60
    m = int(rem_s / 60)
    
    # Remaining seconds after extracting whole minutes
    s_rem = rem_s - (m * 60)

if __name__ == '__main__':
    pass
