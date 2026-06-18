import calendar
from datetime import date

def calculate_duration_days(date1: date, date2: date) -> int:
    """
    Calculates the number of days between two dates, accounting for leap years.
    
    Args:
        date1 (date): The earlier or first date in a 3-digit format 'yyyymmdd'.
        date2 (date): The later or second date in a 3-digit format 'yyyymmdd'.

    Returns:
        int: The absolute number of days between the two dates.

    Raises:
        ValueError: If either input is not a valid date string or if inputs are None/invalid types.
        
    Note: This function converts inputs to datetime.date objects and calculates 
          the difference in days using Python's built-in capabilities, which inherently 
          handles leap year logic correctly without manual calculation of month lengths.
    """
    
    # Ensure we handle both date objects and string representations if needed for flexibility,
    # though strict typing suggests only 'date' is passed here based on docstring hint about format.
    # The problem statement mentions "3-digit format" in the thought block but asks to calculate 
    # duration between dates, implying standard datetime.date usage or custom parsing.
    # To be robust and efficient as requested:
    
    if not isinstance(date1, date) or not isinstance(date2, date):
        raise ValueError("Inputs must be instances of 'datetime.date' objects.")

    delta = abs((date2 - date1).days)
    return delta

if __name__ == '__main__':
    # Hard-coded sample values running without user input
    d1 = date(2023, 5, 15)
    d2 = date(2024, 6, 20)

    duration_days = calculate_duration_days(d1, d2)
    
    print(f"Duration between {d1} and {d2}: {duration_days} days")