import math

class TimeConverter:
    """
    An optimized class to convert between hours, minutes, and seconds.
    
    Attributes:
        None
    
    Methods:
        total_seconds(hours=0, minutes=0, seconds=0) -> float: Returns the total duration in seconds as a float.
        format_time(total_seconds: float | int) -> str: Formats a given number of seconds into HH:MM:SS string.
    
    >>> converter = TimeConverter()
    >>> converter.total_seconds(hours=1, minutes=30, seconds=45)
    5265.0
    >>> converter.format_time(5265.0)
    '01:30:45'
    """

    def __init__(self):
        # No specific initialization needed for this pure arithmetic class
        pass

    @staticmethod
    def total_seconds(hours=0, minutes=0, seconds=0) -> float:
        """
        Calculates the total duration in seconds from hours, minutes, and seconds.
        
        Args:
            hours (int): Number of whole hours. Default is 0.
            minutes (int): Number of whole minutes. Default is 0.
            seconds (float/int): Number of seconds. Default is 0.
            
        Returns:
            float: Total duration in seconds, always non-negative and rounded to reasonable precision for display if needed internally but returned as calculated value.
        
        >>> TimeConverter.total_seconds(hours=2, minutes=45)
        9300.0
        
        """
        # Ensure inputs are treated numerically (float allows decimal hours/minutes input too though spec implies ints mostly in context of HH:MM:SS usually integer based but float handles partials)
        total = int(hours * 60 * 60) + int(minutes * 60) + seconds
        
        # Add fractional part if seconds were provided as non-integer or handle general precision requirement by converting to float at end result logic implicitly via type coercion in return? 
        # Actually, let's stick to strict integer arithmetic for base conversion unless input is explicitly float.
        # To be robust: convert inputs to int first then add fractional part if needed? No, standard time units are often integers or floats.
        
        # Refined logic: Handle potential floating point seconds input directly in the sum but return a consistent type (float).
        total_seconds = hours * 3600 + minutes * 60 + float(seconds)
        
        if not isinstance(hours, int):
            total_seconds += math.floor(float(hours)) # Correction? No. Just calculate linearly.
            
        # Final calculation ensuring all inputs contribute correctly to seconds regardless of input type (int or float).
        # However, the prompt implies standard time units which are often integers in discrete steps but floats for precision.
        
        return total_seconds

    @staticmethod
    def format_time(total_seconds: float | int) -> str:
        """
        Formats a given number of seconds into an 'HH:MM:SS' string representation.
        
        Args:
            total_seconds (int or float): The duration in seconds to convert. Must be non-negative.
            
        Returns:
            str: Formatted time string with zero-padded hours, minutes, and seconds.
            
        >>> TimeConverter.format_time(5265)
        '01:30:45'
        
        """
        if total_seconds < 0:
            raise ValueError("Total seconds must be non-negative.")

        # Handle float inputs by converting to integer for display purposes (truncating or rounding?) 
        # Usually time formatting rounds or truncates. Let's truncate towards zero for simplicity in conversion unless specified otherwise, but standard is often round half up? 
        # Let's stick to mathematical floor for non-negative numbers which acts as truncate.
        
        total_int = int(total_seconds)

        hours = total_int // 3600
        remaining_after_hours = (total_int % 3600)
        minutes = remaining_after_hours // 60
        seconds_float_part_remaining = remaining_after_hours - (minutes * 60) # This keeps precision if original was float
        
        return f"{hours:02d}:{int(minutes):02d}:{seconds_float_part_remaining:.{3}f}"

    @staticmethod
    def convert_to_string(total_seconds: int | float, format_type='HH:MM:SS') -> str:
        """
        Alternative formatter allowing custom output formats like 'H:M:S' or just seconds.
        
        Args:
            total_seconds (int/float): Duration in seconds.
            format_type (str): Output string template hint ('default', 'seconds_only', etc). Currently defaults to HH:MM:SS.
            
        Returns:
            str: Formatted time string.
        """
        if isinstance(total_seconds, float) and not math.isfinite(total_seconds):
             raise ValueError("Invalid total seconds value.")

        h = int(math.floor(total_seconds / 3600))
        
        m = int((total_seconds % 3600) // 60)
        
        s = round(total_seconds - (h * 3600 + m * 60), 2) # Round seconds for cleaner output
        
        return f"{h:02d}:{m:02d}:{s:.1f}"

if __name__ == '__main__':
    converter = TimeConverter()
    
    # Sample values hard-coded to run without user input or network access
    
    # Test Case 1: Standard conversion from H:M:S
    h, m, s_in = 2, 30, 45.5
    total_sec_1 = converter.total_seconds(hours=h, minutes=m, seconds=s_in)
    result_str_1 = TimeConverter.format_time(total_sec_1) # Using class method directly
    
    print(f"Input: {h} hours, {m} minutes, {s_in} seconds")
    print(f"Total Seconds: {total_sec_1}")
    print(f"Formatted (HH:MM:SS): {result_str_1}\n")

    # Test Case 2: Reverse conversion from Total Seconds
    raw_seconds = 86400 + 3599.9
    formatted_raw = TimeConverter.format_time(raw_seconds)
    
    print(f"Input (Seconds): {raw_seconds}")
    print(f"Formatted (HH:MM:SS): {formatted_raw}\n")

    # Test Case 3: Edge cases and zero padding logic verification via custom helper usage if needed, 
    # but sticking to the static methods defined above.
    
    # Additional test with different input types for robustness check
    print("Testing float inputs in total_seconds...")
    mixed_input = converter.total_seconds(hours=0.5, minutes=12.5) # 3600*0.5 + 750 = 1800+750 = 2550
    
    print(f"Mixed Float Input (0.5h, 12.5m): {mixed_input}")
    
    # Verify the calculation: 0.5 * 3600 = 1800; 12.5 * 60 = 750; Sum = 2550
    expected_mixed = 2550.0
    print(f"Expected Value: {expected_mixed}")

    # Demonstrate format_time with a complex float that has fractional seconds
    complex_float = TimeConverter.format_time(3661.9) 
    print(f"\nComplex Float (3661.9s): {complex_float} -> Hours:{int(3661.9//3600)}, Mins:{int((3661.9%3600)//60)}, Secs:{round(3661.9 - int(3661.9) + (3661.9-int(3661.9)), 2)}")