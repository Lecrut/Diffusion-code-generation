"""
Script to calculate time difference between two datetime objects handling time zones correctly using pytz.

This script demonstrates how to convert naive datetimes (without timezone info) into aware 
datetimes using the 'pytz' library, and then calculates the absolute difference in seconds 
between them regardless of their original time zone definitions.
"""

from datetime import datetime
import pytz

def calculate_time_difference(dt1_str: str, dt2_str: str) -> int:
    """
    Calculates the absolute time difference between two datetimes specified as strings.
    
    The function assumes both input strings are in ISO format without timezone information 
    (naive). It converts them to UTC using pytz before calculating the difference to ensure 
    accurate comparison across different potential local times if they were later interpreted differently,
    though here we treat naive inputs by assuming a standard reference or simply converting via 
    pytz's default behavior for naive conversion which often assumes system timezone unless specified.
    
    However, strictly following 'pytz' best practices: to avoid ambiguity with naive datetimes,
    this function will assume the provided strings are in UTC if no offset is present, as per common practice
    when using pytz without explicit zone info on input. Alternatively, we can assign a specific 
    timezone like 'UTC' explicitly for clarity and correctness.
    
    Args:
        dt1_str (str): ISO format string of the first datetime (e.g., "2023-10-05 14:30").
        dt2_str (str): ISO format string of the second datetime (e.g., "2023-10-06 08:15").
        
    Returns:
        int: The absolute time difference in seconds.
    """
    
    # Define a reference timezone for naive datetimes to ensure they are treated consistently.
    # Using UTC is the safest default when no timezone info is provided on input strings.
    tz = pytz.UTC
    
    try:
        dt1_naive = datetime.fromisoformat(dt1_str)
        dt2_naive = datetime.fromisoformat(dt2_str)
        
        # Convert naive datetimes to aware datetimes in UTC using pytz
        dt1_utc = tz.localize(dt1_naive, is_dst=None)
        dt2_utc = tz.localize(dt2_naive, is_dst=None)
        
        difference_seconds = abs((dt2_utc - dt1_utc).total_seconds())
        
    except ValueError as e:
        raise ValueError(f"Invalid datetime format provided. Expected ISO 8601 without timezone.") from e
        
    return int(difference_seconds)

if __name__ == '__main__':
    # Hard-coded sample values for testing purposes.
    # These are naive datetimes in ISO format representing specific moments in time.
    
    dt_sample_1 = "2023-10-05 14:30"
    dt_sample_2 = "2023-10-06 08:15"
    
    # Calculate the difference and print the result.
    time_diff_seconds = calculate_time_difference(dt_sample_1, dt_sample_2)
    
    print(f"The absolute time difference between {dt_sample_1} and {dt_sample_2} is:")
    print(f"{time_diff_seconds} seconds.")