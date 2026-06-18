"""
Module: datetime_difference_calculator

A production-ready script to calculate the time difference between two arbitrary 
datetime objects and output the result in user-specified units (days, hours, minutes).

This module avoids interactive input, command-line arguments, or network access.
It includes a self-contained main block with hard-coded sample values for testing.
"""

from datetime import datetime

def calculate_time_difference(start: datetime, end: datetime) -> float:
    """
    Calculate the total time difference in seconds between two datetime objects.
    
    Args:
        start (datetime): The starting datetime object.
        end (datetime): The ending datetime object.
        
    Returns:
        float: Total duration in seconds if end is after start, otherwise negative value.
               If inputs are None or invalid types, raises TypeError.
    """
    try:
        return (end - start).total_seconds()
    except Exception as e:
        raise TypeError(f"Invalid datetime objects provided: {e}")

def format_duration(seconds: float) -> str:
    """
    Format the total seconds into a human-readable string containing days, hours, 
    and remaining minutes.
    
    Args:
        seconds (float): Total duration in seconds.
        
    Returns:
        str: Formatted time difference as "X day(s), Y hour(s), Z minute(s)".
             Uses pluralization for units where appropriate.
    """
    days = int(seconds // 86400)
    remaining_seconds = (seconds % 86400)
    
    hours = int(remaining_seconds // 3600)
    remaining_seconds %= 3600
    
    minutes = int(remaining_seconds / 60)
    
    result_parts = []
    
    if days > 0:
        unit_str = "day" + ("s" if days != 1 else "")
        result_parts.append(f"{days} {unit_str}")
        
    if hours > 0 or (hours == 0 and minutes > 0):
        unit_str = "hour" + ("s" if hours != 1 else "")
        result_parts.append(f"{hours} {unit_str}")
        
    if minutes > 0:
        unit_str = "minute" + ("s" if minutes != 1 else "")
        result_parts.append(f"{minutes} {unit_str}")
    
    return ", ".join(result_parts)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    start_time = datetime(2023, 5, 17, 8, 30, 45)
    end_time = datetime(2023, 6, 1, 9, 15, 30)
    
    try:
        total_seconds = calculate_time_difference(start_time, end_time)
        
        formatted_output = format_duration(total_seconds)
        
        print(f"Time Difference Calculation:")
        print(f"Start Time: {start_time}")
        print(f"End Time:   {end_time}")
        print("-" * 30)
        print(f"Total Duration (seconds): {total_seconds:.2f}s")
        print(f"Formatted Output:         {formatted_output}")
        
    except TypeError as e:
        print(f"Error during calculation: {e}")