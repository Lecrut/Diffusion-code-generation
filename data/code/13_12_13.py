import datetime

def scale_time_differences(time_diff_strings):
    """
    Converts a list of time difference strings into standardized timedelta objects.
    
    Handles common string formats (e.g., "1 day", "-2 hours 30 minutes") and 
    gracefully ignores invalid entries by filtering them out rather than raising errors on the whole list.
    
    Args:
        time_diff_strings (list[str]): List of strings representing time differences.
        
    Returns:
        list[datetime.timedelta]: A list containing only successfully parsed timedelta objects.
    """
    result = []

if __name__ == '__main__':
    pass
