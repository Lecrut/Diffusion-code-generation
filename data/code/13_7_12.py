import calendar
from datetime import date

def calculate_duration_days(start_date: date, end_date: date) -> int:
    """
    Calculate the number of days between two dates, handling leap years accurately.
    
    Args:
        start_date (date): The starting date.
        end_date (date): The ending date.
        
    Returns:
        int: The absolute difference in days between the two dates.
    """
    # Ensure we are calculating forward duration for simplicity, 
    # though logic works regardless of order if taking abs at the end.
    
    total_days = 0
    
    current_year = start_date.year
    target_year = end_date.year
    
    while True:
        next_day = date(current_year + 1, 1, 1) - date(current_year, 1, 1)

if __name__ == '__main__':
    pass
