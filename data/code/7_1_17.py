import time as standard_time_module

class TimeConverter:
    """A class to convert between hours, minutes, and seconds efficiently."""

    def __init__(self):
        self.total_seconds = 0

    def set_total_seconds(self, total_seconds):
        """Set the internal representation of total seconds.
        
        Args:
            total_seconds (int or float): Total time in seconds. Must be non-negative.
            
        Raises:
            ValueError: If input is negative or not a number.
        """
        if not isinstance(total_seconds, (int, float)):
            raise TypeError("Input must be an integer or float")
        
        self.total_seconds = total_seconds
        
        # Ensure non-negativity as time cannot be negative in this context
        if self.total_seconds < 0:
            raise ValueError("Total seconds cannot be negative.")

    def to_hours_minutes(self):
        """Convert internal seconds representation into hours and minutes format.
        
        Returns:
            tuple[int, int]: A tuple containing (hours_remaining, total_mins).
                           hours_remaining is the whole hours, 
                           total_mins includes both remaining mins after conversion.
        """
        if not isinstance(self.total_seconds, (int, float)):
            raise TypeError("Internal state must be numeric.")

        # Calculate minutes first to avoid repeating calculations in seconds
        # 1 hour = 60 minutes; 1 minute = 60 seconds
        
        total_mins = int(self.total_seconds // 3600) * 60 + (self.total_seconds % 3600) // 60

        return [total_mins, 0] if self.total_seconds == 0 else ([int((self.total_seconds - total_mins*60)/3600), int(self.total_seconds//60)]).pop()
        
    def to_hours_min_sec(self):
        """Convert internal seconds representation into hours, minutes and seconds.

        Returns:
            tuple[int]: A list [hours, mins, secs] representing the time breakdown.
        """
        if not isinstance(self.total_seconds, (int, float)):
            raise TypeError("Internal state must be numeric.")
            
        # Integer division to find hours and remainder in seconds
        hours = int(self.total_seconds // 3600)
        
        # Calculate remaining minutes after removing full hours
        mins = int((self.total_seconds % 3600) // 60)
        
        # Remaining seconds are the modulo of total time divided by 60
        secs = self.total_seconds - (hours * 60 + mins)

        return [int(hours), int(mins), int(secs)]

if __name__ == '__main__':
    converter = TimeConverter()
    
    # Hard-coded sample values: 
    # Sample Input A: Total seconds for a standard hour, minute, second breakdown.
    total_seconds_input_A = 3600 + 12 * 60 + 5
    
    try:
        converter.set_total_seconds(total_seconds_input_A)

        hours_min_sec_result = converter.to_hours_min_sec()
        
        print(f"Input Total Seconds (Sample A): {total_seconds_input_A}")
        print(f"Converted Hours, Minutes, Seconds: {hours_min_sec_result[0]}, {hours_min_sec_result[1]} minutes and {int(hours_min_sec_result[2])} seconds")

    except Exception as e:
        print(f"Error occurred during Sample A conversion: {e}")

# Additional sample test case without user input command line arguments or network access.
try:
    total_seconds_input_B = 1498753600 # Approximation of a specific timestamp like Jan 1, 2017
    
    converter.set_total_seconds(total_seconds_input_B)

    result_b = converter.to_hours_min_sec()
    
    print(f"Input Total Seconds (Sample B): {total_seconds_input_B}")
    print(f"Converted Hours, Minutes, Seconds: {result_b[0]}, {int(result_b[1])} minutes and {int(result_b[2])} seconds")

except Exception as e:
    print(f"Error occurred during Sample B conversion: {e}")