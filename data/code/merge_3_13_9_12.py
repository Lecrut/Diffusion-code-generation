import time
from datetime import datetime, timedelta

class TimeScaleConverter:
    """
    A simple class to handle conversion between Pacific Standard Time (PST) 
    and Eastern Standard Time (EST). Note that in standard practice, these are 
    UTC offsets of -8 hours and -5 hours respectively. This implementation assumes 
    fixed offset logic as per the prompt's request for 'time scale logic' without 
    explicit timezone database dependencies or DST handling complexity unless specified.
    
    PST Offset: UTC-8
    EST Offset: UTC-5
    
    The difference between EST and PST is 3 hours (EST is ahead).
    """

    def __init__(self):
        self.pst_offset_hours = -8
        self.est_offset_hours = -5

    def convert_pst_to_est(self, pst_datetime_str):
        """
        Converts a datetime string in PST format to EST.
        
        Args:
            pst_datetime_str (str): A date-time string representing the time in PST 
                                   (e.g., "2023-10-05 14:30"). The year is assumed fixed 
                                   for this simple logic or can be parsed if provided fully.
        
        Returns:
            datetime: The converted datetime object in EST.
        """
        # Parse the input string into a naive datetime object (no timezone info attached yet)
        dt_pst = datetime.strptime(pst_datetime_str, "%Y-%m-%d %H:%M")

        # Calculate the difference between PST and EST offsets
        offset_difference_hours = self.est_offset_hours - self.pst_offset_hours
        
        # Create a timedelta object representing the 3-hour shift (EST is ahead)
        time_diff = timedelta(hours=offset_difference_hours)

        # Add the difference to the original datetime to get EST time
        dt_est = dt_pst + time_diff

        return dt_est, offset_difference_hours

def main():
    """
    Main execution block demonstrating the TimeScaleConverter logic.
    Uses hard-coded sample values as per requirements (no input(), sys.stdin, etc.).
    """
    
    # Initialize the converter
    converter = TimeScaleConverter()

    # Hard-coded sample value representing a time in PST format
    pst_sample_time_str = "2023-10-05 14:30"

    print(f"Input Time (PST): {pst_sample_time_str}")

    # Perform the conversion and get both the EST datetime and the difference hours
    est_datetime, time_diff_hours = converter.convert_pst_to_est(pst_sample_time_str)

    # Format the output for display
    formatted_est_time = est_datetime.strftime("%Y-%m-%d %H:%M")

    print(f"Converted Time (EST): {formatted_est_time}")
    
    if abs(time_diff_hours) > 0:
        direction = "ahead by" if time_diff_hours > 0 else "behind by"
        magnitude = f"{abs(time_diff_hours)} hour(s)"
        print(f"Time Difference: EST is {direction} PST by {magnitude}")

if __name__ == '__main__':
    main()