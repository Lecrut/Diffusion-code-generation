import argparse
from datetime import timedelta

def calculate_elapsed_time(start_str: str, end_str: str, unit: str = 'minutes') -> float:
    """
    Calculates the elapsed time between two ISO format strings and returns the duration in specified units.
    
    Args:
        start_str (str): Start date/time string (ISO 8601 recommended).
        end_str (str): End date/time string (ISO 8601 recommended).
        unit (str): Output unit ('seconds', 'minutes', or 'hours'). Default is 'minutes'.

    Returns:
        float: Elapsed time in the specified unit.
    
    Note: This function does not use command-line arguments; it performs a direct calculation based on provided values.
    """
    start = timedelta.fromisoformat(start_str)
    end = timedelta.fromisoformat(end_str)
    elapsed_seconds = (end - start).total_seconds()

    unit_map = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600
    }

    return elapsed_seconds / unit_map[unit]

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input or external dependencies.
    start_time = "2024-01-01T08:00:00"  # Start time in ISO format string.
    end_time = "2024-01-01T09:30:00"   # End time in ISO format string.
    desired_unit = 'minutes'            # Desired output unit for the elapsed time calculation.

    result_duration = calculate_elapsed_time(start_time, end_time, desired_unit)
    print(f"The total elapsed time is {result_duration} units.")