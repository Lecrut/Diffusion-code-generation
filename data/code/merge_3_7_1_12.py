class TimeConverter:
    """A class to convert between hours, minutes, and seconds efficiently."""

    def __init__(self):
        pass

    def total_seconds(self, hours=0, minutes=0, seconds=0) -> float:
        """Calculate the total number of seconds from given time components.
        
        Args:
            hours (int or float): Number of hours. Defaults to 0.
            minutes (int or float): Number of minutes. Defaults to 0.
            seconds (float): Number of seconds. Defaults to 0.
            
        Returns:
            float: Total time in seconds.
        """
        return hours * 3600 + minutes * 60 + seconds

    def total_minutes(self, hours=0, minutes=0, seconds=0) -> float:
        """Calculate the total number of minutes from given time components.
        
        Args:
            hours (int or float): Number of hours. Defaults to 0.
            minutes (int or float): Number of minutes. Defaults to 0.
            seconds (float): Number of seconds. Defaults to 0.
            
        Returns:
            float: Total time in minutes.
        """
        return hours * 60 + minutes + seconds / 60

    def total_hours(self, hours=0, minutes=0, seconds=0) -> float:
        """Calculate the total number of hours from given time components.
        
        Args:
            hours (int or float): Number of hours. Defaults to 0.
            minutes (int or float): Number of minutes. Defaults to 0.
            seconds (float): Number of seconds. Defaults to 0.
            
        Returns:
            float: Total time in hours.
        """
        return hours + minutes / 60 + seconds / 3600

    def format_time(self, total_seconds: int) -> str:
        """Format a given number of seconds into the HH:MM:SS string representation.
        
        Args:
            total_seconds (int): Total time in seconds.
            
        Returns:
            str: Formatted time string 'HH:MM:SS'.
        """
        hours = int(total_seconds // 3600)
        remainder = total_seconds % 3600
        minutes = int(remainder // 60)
        seconds = int(remainder % 60)
        
        return f"{hours:02}:{minutes:02}:{seconds:02}"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    converter = TimeConverter()

    print("Sample Conversions:")

    # Sample 1: Convert specific time components to total seconds and minutes
    h, m, s = 2, 30, 45
    secs_total = converter.total_seconds(h, m, s)
    mins_total = converter.total_minutes(h, m, s)
    hrs_total = converter.total_hours(h, m, s)

    print(f"Input: {h} hours, {m} minutes, {s} seconds")
    print(f"Total Seconds: {secs_total}")
    print(f"Total Minutes: {mins_total:.2f}")
    print(f"Total Hours: {hrs_total:.4f}\n")

    # Sample 2: Convert total seconds to formatted time string
    test_seconds = int(secs_total)
    formatted_time = converter.format_time(test_seconds)
    print(f"{test_seconds} seconds formatted as: {formatted_time}")

    # Sample 3: Verify round-trip conversion accuracy with a large value
    large_input_hours, large_input_minutes, large_input_seconds = 10, 59, 59
    original_total_sec = converter.total_seconds(large_input_hours, large_input_minutes, large_input_seconds)
    
    # Reconstruct from total seconds to verify precision
    reconstructed_hrs = int(original_total_sec // 3600)
    remainder_after_hrs = original_total_sec % 3600
    reconstructed_mins = int(remainder_after_hrs // 60)
    reconstructed_secs = int(remainder_after_hrs % 60)

    print(f"Large Input: {large_input_hours}h, {large_input_minutes}m, {large_input_seconds}s")
    print(f"Reconstructed from total seconds:")
    print(f"Hours: {reconstructed_hrs}, Minutes: {reconstructed_mins}, Seconds: {reconstructed_secs}")
    
    # Check if reconstruction matches original (allowing for floating point epsilon in logic)
    diff = abs((large_input_hours - reconstructed_hrs)*3600 + 
               (large_input_minutes - reconstructed_mins)*60 + 
               (large_input_seconds - reconstructed_secs))
    print(f"Reconstruction Error: {diff} seconds")