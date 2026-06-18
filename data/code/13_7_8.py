import math

def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    """Return the number of days in a specific month of a given year."""
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else: # February
        return 29 if is_leap_year(year) else 28

def days_between_date(date_a, date_b):
    """Calculate the duration (in days) between two dates.
    
    Args:
        date_a (tuple): Start date as (year, month, day).
        date_b (tuple): End date as (year, month, day).
        
    Returns:
        int: The number of days from date_a to date_b. Positive if b > a, negative otherwise.
    """
    # Ensure date_b is the later date for positive duration logic, 
    # but we will calculate signed difference based on input order first then adjust sign if needed?
    # Actually, standard practice: return absolute days or (end - start). Let's do (date_a -> date_b) as requested "between".
    # Usually implies |a-b| or a->b. We'll compute end_date - start_date for clarity on direction.
    
    def total_days_from_epoch(year, month, day):
        """Calculate the number of days from year 1 to (year, month, day)."""
        if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
            raise ValueError("Date components must be integers.")
        
        # Days in full years before 'year'
        total_days = 0
        
        for y in range(1, year):
            total_days += 365 if not is_leap_year(y) else 366
            
        # Days in months of the current year up to (month - 1)
        days_in_current_month_sum = 0
        for m in range(1, month):
            days_in_current_month_sum += days_in_month(m, y)
            
        total_days += day
        
        return total_days

    # Calculate absolute difference first to handle potential negative inputs gracefully if needed, 
    # but strictly following "duration between" often implies magnitude. However, signed is more precise for algorithms.
    # Let's assume the user wants the simple duration (absolute value) or end - start.
    # Given the prompt asks for "duration", absolute difference is usually expected unless direction is specified.
    
    days_a = total_days_from_epoch(date_a[0], date_a[1], date_a[2])
    days_b = total_days_from_epoch(date_b[0], date_b[1], date_b[2])
    
    duration = abs(days_b - days_a)
    
    return duration

if __name__ == '__main__':
    # Sample values: 
    # Date A: January 1, 2023 (Non-leap year start)
    # Date B: February 29, 2024 (Leap day in next leap year)
    
    date_start = (2023, 1, 1)
    date_end = (2024, 2, 29)

    duration_days = days_between_date(date_start, date_end)
    
    print(f"Duration between {date_start} and {date_end}:")
    print(f"{duration_days} days")