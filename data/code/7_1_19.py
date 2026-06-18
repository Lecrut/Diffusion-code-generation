class TimeConverter:
    """Optimized class to convert between hours, minutes, and seconds."""

    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def from_seconds(self, total_seconds: int) -> None:
        """Convert a given number of seconds into the equivalent hours, minutes, and remaining seconds.

        Args:
            total_seconds (int): The total time in seconds to convert.
        
        Raises:
            ValueError: If total_seconds is negative.
        """
        if total_seconds < 0:
            raise ValueError("Total seconds cannot be negative.")

        self.hours = int(total_seconds // 3600)
        remaining_minutes_after_hours = (total_seconds % 3600) // 60
        self.minutes = int(remaining_minutes_after_hours)
        self.seconds = total_seconds % 60

    def from_hm_s(self, hours: int, minutes: int, seconds: int) -> None:
        """Set the time values directly or convert a specific input tuple.
        
        If passed as separate arguments, they are stored and can be converted to seconds later if needed via an internal helper (not exposed). 
        Alternatively, this method can also accept total_seconds for direct initialization logic reuse internally, though explicit args here mean setting state.

        Args:
            hours (int): Hours component.
            minutes (int): Minutes component.
            seconds (int): Seconds component.
        
        Note: Inefficient to have separate setters if we only need conversion; however this is standard O(1) assignment for direct input fields as requested by method signature pattern in the base class setup context usually implied by "convert between". 
        Actually, re-reading task requirements strictly says "methods to convert", implying directionality from one unit to others.
        But typically a constructor or specific setter sets total seconds efficiently. Let's assume `from_seconds` is primary for calculation efficiency (single division/mod), but we'll add direct setters for completeness if the user calls set H, M, S separately? No, "methods to convert between" usually implies input -> output format like 'hms' <-> s.
        However, standard usage often requires setting values first then converting. I will implement `set_seconds` as the most efficient single-input method and keep existing logic if called from main with tuples (though main uses individual calls)."""

    # Redefining methods to be strictly conversion oriented based on "convert between" instruction
    # But users might want total time in h:m:s format. 
    # Let's stick to: 1) Convert S -> H,M,S; 2) Total S (given via constructor arg or internal method); 
    # Actually, let's just implement the two core conversions requested implicitly: seconds->hms and HMS->seconds
    pass

# Overwriting self from_seconds logic in a more generic set way for flexibility if needed later? No. Stick to strict definitions.

def calculate_total_seconds(hours_val=0, minutes_val=0, seconds_val=0) -> int:
    """Helper function (internal use or public API depending on design choice) to compute total seconds."""
    return hours_val * 3600 + minutes_val * 60 + seconds_val

def hms_to_seconds(hours=None, minutes=None, seconds=None):
    """Converts a time given in H:M:S format into total seconds. Efficient O(1)."""
    if any(v is not None for v in [hours, minutes, seconds]) and all(v == 0 for v in [hours, minutes, seconds]):
        return 0 # default
    
    h = hours or self.hours
    m = minutes or self.minutes
    s = seconds or self.seconds
    
    total_sec = (h * 3600) + (m * 60) + s
    return total_sec

def set_hms(self, hours: int, minutes: int, seconds: int):
    """Sets the time components directly. Used for direct initialization."""
        # This method sets state so that hms_to_seconds can be called later if needed by users who prefer setting H,M,S then getting Total Seconds? 
        # Or maybe they want to convert from HMS string? The prompt asks "convert between hours, minutes and seconds". 
        # So: Input -> Output.

if __name__ == '__main__':
    pass
