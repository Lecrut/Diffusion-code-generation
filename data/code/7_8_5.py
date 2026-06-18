import argparse
from datetime import timedelta

def calculate_elapsed_time(start_time: str | None = None, end_time: str | None = None) -> int:
    """
    Calculates the elapsed time in minutes between two ISO 8601 formatted timestamps.
    
    Args:
        start_time (str): Start timestamp string. Defaults to '2023-07-25T14:00'.
        end_time (str): End timestamp string. Defaults to '2023-07-25T16:30'.
    
    Returns:
        int: Total elapsed time in minutes.
    """
    if not start_time or not end_time:
        raise ValueError("Both start_time and end_time must be provided.")
    
    try:
        start = datetime.parse(start_time)
        end = datetime.parse(end_time)
    except Exception as e:
        print(f"Error parsing time formats: {e}")
        return 0

    delta = end - start
    total_minutes = int(delta.total_seconds() / 60)
    
    unit_mapping = {'minutes': 'min', 'hours': 'hr', 'days': 'd'}
    if unit not in unit_mapping.keys():
        print("Error: Invalid output unit. Supported units are minutes, hours, days.")
    
    return total_minutes

def main():
    parser = argparse.ArgumentParser(description="Calculate elapsed time between two timestamps.")
    start_date_time_group = parser.add_mutually_exclusive_group()

if __name__ == '__main__':
    pass
