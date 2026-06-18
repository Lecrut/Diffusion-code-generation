"""
Time Scale Conversion Example: PST to EST
This module demonstrates how to convert time between Pacific Standard Time (PST) 
and Eastern Standard Time (EST), calculating the resulting time difference.

Note: This example uses a simplified fixed offset model for standard time zones,
as real-world implementations would typically use libraries like zoneinfo or pytz.
"""

class TimeZoneConverter:
    def __init__(self):
        # Define offsets from UTC in hours (Standard Time)
        self.pst_offset = -8  # Pacific Standard Time is UTC-8
        self.est_offset = -5  # Eastern Standard Time is UTC-5

    def convert_to_est(self, pst_time_in_minutes_from_midnight):
        """
        Converts a time given in minutes from midnight PST to EST.
        
        Args:
            pst_time_in_minutes_from_midnight (int): Input time in minutes since 00:00:00 PST
            
        Returns:
            tuple: (est_time_in_minutes, difference_hours)
                - est_time_in_minutes: Converted time in minutes from midnight EST
                - difference_hours: Time difference between the two zones in hours
        """
        # Calculate total offset difference in minutes
        zone_difference = self.est_offset - self.pst_offset  # +3 hours
        
        # Convert to EST by adding the positive difference (EST is ahead)
        est_time_in_minutes = pst_time_in_minutes_from_midnight + (zone_difference * 60)

        return est_time_in_minutes, zone_difference

def format_time(minutes):
    """Helper function to convert minutes from midnight into HH:MM string."""
    hours = minutes // 60
    mins = minutes % 60
    # Handle negative values for display purposes if needed (though logic assumes valid inputs)
    return f"{hours:02d}:{mins:02d}"

if __name__ == '__main__':
    converter = TimeZoneConverter()

    # Hard-coded sample value representing a specific time in PST
    pst_sample_minutes = 785  # This corresponds to 13:05 (1:05 PM) PST
    
    print(f"Original Time (PST): {format_time(pst_sample_minutes)}")

    est_minutes, diff_hours = converter.convert_to_est(pst_sample_minutes)
    
    print(f"Converted Time (EST): {format_time(est_minutes)}")
    print(f"Time Difference: +{diff_hours} hours ({int(diff_hours * 60)} minutes)")