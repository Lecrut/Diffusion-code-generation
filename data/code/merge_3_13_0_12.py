import pytz
from datetime import datetime

def calculate_time_difference(start_dt: datetime, end_dt: datetime) -> float:
    """
    Calculates the time difference in seconds between two timezone-aware datetime objects.
    
    Args:
        start_dt (datetime): The starting datetime object with explicit timezone info.
        end_dt (datetime): The ending datetime object with explicit timezone info.
        
    Returns:
        float: Time difference in seconds (positive if end_dt is after start_dt).
    """
    # Ensure both datetimes are aware of their timezones to avoid ambiguous calculations.
    # If they were created without knowing the zone, pytz will be used for local normalization here.
    
    diff = end_dt - start_dt
    
    return diff.total_seconds()

def main():
    """
    Main execution block with hard-coded sample values demonstrating timezone handling.
    This script runs entirely offline and requires no user input or command-line arguments.
    It uses 'pytz' to correctly handle US Eastern Time (EST/EDT) vs UTC conversion logic,
    although for fixed historical dates the DST offset is implicitly handled by pytz's localize().
    
    Sample Case:
        Start: January 15, 2023 at 8:00 AM in New York (UTC-5 during EST).
        End:   February 14, 2023 at 6:00 PM in UTC.
        
    Expected Logic Verification:
        - pytz will correctly apply the fixed offset for January 1st (EST = UTC-5).
        - The second datetime is already specified as 'UTC', so no conversion needed there.
        - The difference should reflect the actual elapsed time, not just naive hour subtraction.
    """

    # Sample Start Date: New York City on Jan 15, 2023 (EST)
    new_york_tz = pytz.timezone('US/Eastern')
    start_dt = new_york_tz.localize(datetime(2023, 1, 15, 8, 0, 0))

    # Sample End Date: UTC on Feb 14, 2023
    utc_tz = pytz.UTC
    end_dt = utc_tz.localize(datetime(2023, 2, 14, 18, 0, 0))

    print("Calculating time difference...")
    
    # Calculate the raw duration in seconds between the two aware datetimes.
    diff_seconds = calculate_time_difference(start_dt, end_dt)
    
    # Convert to hours for readability
    diff_hours = abs(diff_seconds / 3600)

    print(f"Start Time: {start_dt}")
    print(f"End Time:   {end_dt}")
    print(f"Difference (seconds): {diff_seconds:.2f}")
    print(f"Difference (hours):   {diff_hours:.4f} hours")

if __name__ == '__main__':
    main()