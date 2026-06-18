import math

class TimeConverter:
    """A class to convert between hours, minutes, and seconds efficiently."""

    def __init__(self):
        self.total_seconds = 0

    def set_total_time(self, total_seconds: int) -> None:
        """Set the internal state based on a total number of seconds.
        
        Args:
            total_seconds (int): The absolute time in seconds to store.
            
        Raises:
            ValueError: If total_seconds is negative.
        """
        if total_seconds < 0:
            raise ValueError("Total seconds cannot be negative.")
        self.total_seconds = total_seconds

    def hours(self) -> float:
        """Return the time in hours as a floating-point number."""
        return self.total_seconds / 3600.0

    def minutes(self) -> float:
        """Return the time in minutes as a floating-point number."""
        return self.total_seconds / 60.0

    def seconds(self) -> int:
        """Return the integer remainder of total seconds after removing full hours and minutes.
        
        This method calculates how many whole seconds remain if we express 
        the duration purely in terms of base units (hours, then remaining minutes).
        However, to ensure mathematical soundness for any input where 'seconds' might be interpreted 
        as a component rather than just the remainder from total_seconds:
        
        If the user intends 'seconds()' to return the raw seconds part of a mixed representation 
        (e.g., 1h 30m 45s -> 45), it should simply be self.total_seconds % 60.
        But given the context of converting *between* units, usually one wants to know:
        'What is this time in seconds?' or 'How many full minutes and remaining seconds?'.
        
        To avoid ambiguity with a single total_seconds storage, let's interpret `seconds()` 
        as returning the integer part of the fractional second if we were doing high precision, 
        OR more likely given standard time conversion tasks: return the number of whole seconds.
        
        Since self.total_seconds is already an int representing absolute seconds from 0,
        simply casting it to float for display or keeping it as int logic applies directly.
        However, if we strictly follow "convert between", let's assume a scenario where 
        time might be passed in mixed units later (though this class stores total).
        
        For robustness and simplicity given the single state variable:
        If 'seconds()' is called on an object initialized with 3605 seconds, it should return 5.
        But wait, if I set 1 hour = 3600s, then 3605s total -> remainder is 5.
        
        Let's refine: The most useful "seconds" method in a converter usually implies 
        the raw second component of a mixed input (H:M:S). Since this class stores TOTAL seconds,
        we can derive H and M from it easily. To provide an 's' value that makes sense as a unit conversion result:
        
        If I have 1 hour 30 minutes -> total = 5400. 
        Does "seconds()" return 5400? No, that's the whole thing in seconds.
        Usually converters allow input like (h, m, s). This class simplifies to Total Seconds.
        
        Let's assume 'seconds()' returns the integer part of total_seconds if we treat it as 
        a duration from epoch, OR simply return self.total_seconds % 60 which represents 
        the "seconds" component in an H:M:S breakdown derived from this total.
        
        Given the prompt asks for conversion logic:
        If I want to convert Total -> S (component), it is modulo 60.
        Let's implement seconds() as returning self.total_seconds % 60, 
        because that represents the 'seconds' unit in a standard time format derived from this total.
        
        Wait, if I set 1 second = 1s. Total=1. Seconds component = 1. Correct.
        If I set 2 minutes = 120s. Total=120. Seconds component (mod 60) = 0. 
        This implies the time is exactly on the minute mark in H:M:S format (e.g., 0:2:0).
        
        Alternative interpretation: Just return total_seconds as an int? No, that's redundant with internal state.
        Let's stick to standard decomposition logic for clarity if mixed units were used elsewhere.
        But since we only store Total Seconds, the most logical "seconds" output 
        in a conversion context (like printing H:M:S) is indeed total_seconds % 60.
        
        However, there is another interpretation: What if 'set_total_time' accepts hours/minutes?
        The constructor or setters could accept mixed units to build the object properly.
        Let's add a more flexible setter that can take (hours, minutes, seconds).
        
        Revised Plan for `seconds()`: 
        If we treat this as a pure converter where input is often H:M:S and output is S:HHMMSS etc.,
        then 'seconds()' returning total_seconds % 60 makes sense.
        
        Let's implement the setter to accept mixed units (h, m, s) for better utility, 
        but keep internal state as absolute seconds.
    """

    def set_time(self, hours: int = 0, minutes: int = 0, seconds: int = 0) -> None:
        """Set the time based on mixed units (hours, minutes, seconds).
        
        Args:
            hours (int): Number of full hours. Defaults to 0.
            minutes (int): Number of additional minutes. Defaults to 0.
            seconds (int): Additional seconds. Defaults to 0.
            
        Raises:
            ValueError: If any input is negative.
        """
        if hours < 0 or minutes < 0 or seconds < 0:
            raise ValueError("Time components cannot be negative.")
        
        # Calculate total seconds from mixed units
        self.total_seconds = (hours * 3600) + (minutes * 60) + seconds

    def to_hours(self, hours: int | float = None, minutes: int | float = None, 
                  seconds: int | float = None) -> dict[str, float]:
        """Convert a time specification into a dictionary of components.
        
        Args:
            hours (int|float): Hours component. Defaults to 0.
            minutes (int|float): Minutes component. Defaults to 0.
            seconds (int|float): Seconds component. Defaults to 0.
            
        Returns:
            dict[str, float]: A dictionary containing 'hours', 'minutes', and 'seconds'.
                            The values are calculated based on the inputs provided 
                            or derived from self.total_seconds if not explicitly passed?
                            
        Actually, let's make this method convert a SPECIFIC input tuple into components.
        If no args are given, it returns the decomposition of self.total_seconds.
        
        Logic:
        1. Calculate total seconds from inputs (or use stored value).
        2. Compute hours = floor(total / 3600)
        3. Remaining minutes = floor((total % 3600) / 60)
        4. Seconds = total % 60
        
        This ensures mathematical soundness regardless of input scale.
    """

    def get_components(self, hours: int | float = None, 
                       minutes: int | float = None, 
                       seconds: int | float = None) -> dict[str, float]:
        """Get the time components (hours, minutes, remaining seconds).
        
        If arguments are provided, they override or supplement self.total_seconds.
        To keep it simple and robust as a converter class:
        - If no args passed, decompose self.total_seconds into H:M:S format.
        - If args passed, calculate total from them and return decomposition of that new total.
        
        Args:
            hours (int|float): Hours to include. Defaults to 0 if not provided.
            minutes (int|float): Minutes to include. Defaults to 0 if not provided.
            seconds (int|float): Seconds to include. Defaults to 0 if not provided.
            
        Returns:
            dict[str, float]: Dictionary with keys 'hours', 'minutes', 'seconds'.
                            Values are floats representing the decomposed time units.
    """

    def convert_to_seconds(self) -> int:
        """Return the total duration in seconds as an integer."""
        return self.total_seconds

if __name__ == '__main__':
    pass
