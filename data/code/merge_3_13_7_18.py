import datetime

def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    """Return the number of days in a specific month of a given year."""
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:  # February
        if is_leap_year(year):
            return 29
        return 28

def calculate_duration_days(date1_str, date2_str):
    """
    Calculate the duration in days between two dates given as strings.
    
    Args:
        date1_str (str): First date string in 'YYYY-MM-DD' format.
        date2_str (str): Second date string in 'YYYY-MM-DD' format.
        
    Returns:
        int: Duration in days from date1 to date2. If negative, it means the duration is backwards.
             The function handles leap years accurately by calculating cumulative day counts manually 
             rather than relying solely on datetime differences which might have edge cases with timezone or calendar rules.
    
    Raises:
        ValueError: If input strings are not in 'YYYY-MM-DD' format.
    """
    def parse_date(date_str):
        try:
            parts = date_str.split('-')
            if len(parts) != 3:
                raise ValueError("Date must be in YYYY-MM-DD format")
            
            year, month, day = map(int, parts)
            
            # Basic validation for leap years and valid dates is done here to ensure accuracy before calculation
            max_day_in_month = days_in_month(year, month)
            if not (1 <= month <= 12):
                raise ValueError("Invalid month")
            elif day < 1 or day > max_day_in_month:
                raise ValueError(f"Invalid day for {year}-{month}")
                
            return year, month, day
            
        except Exception as e:
            if "ValueError" in str(type(e)):
                raise
            else:
                raise ValueError("Date string is invalid") from e

    d1 = parse_date(date1_str)
    d2 = parse_date(date2_str)
    
    # Calculate total days from a reference point (e.g., year 0, month 1, day 1 - though Python handles negative years in datetime too)
    def get_days_from_epoch(year, month, day):
        total_days = 0
        
        # Add days for full years before the current one
        for y in range(0, year):
            if is_leap_year(y):
                total_days += 366
            else:
                total_days += 365
                
        # Add days for full months in the current year
        for m in range(1, month):
            total_days += days_in_month(year, m)
            
        # Add days from the start of the current month to the day (inclusive logic adjusted later if needed, 
        # but here we count up to the end of previous months + current day - 1 for difference calculation usually.
        # Actually, let's just sum: all full years before Y, all full months in year < M, and days passed in month)
        
        return total_days

    days_from_epoch_1 = get_days_from_epoch(d1[0], d1[1], 1) + (d1[2] - 1) # Subtracting 1 because we count from start of day to end of previous day for diff logic effectively, or simply:
    
    # Let's re-calculate more robustly without the epoch offset confusion. 
    # We will calculate absolute days since a fixed point (e.g., Jan 1st Year 0) manually.
    
    def count_absolute_days(y, m, d):
        total = 0
        for y_prev in range(0, y):
            if is_leap_year(y_prev):
                total += 366
            else:
                total += 365
        
        # Days in months before current month of current year
        days_before_month = sum(days_in_month(y, i) for i in range(1, m))
        
        return total + days_before_month + d - 1

    abs_days_1 = count_absolute_days(d1[0], d1[1], d1[2])
    abs_days_2 = count_absolute_days(d2[0], d2[1], d2[2])
    
    duration = abs_days_2 - abs_days_1
    
    return duration

if __name__ == '__main__':
    # Sample values to test leap year handling and date calculation
    sample_date1_str = "2023-02-28"  # Non-leap year end of February
    sample_date2_str = "2024-03-01"  # Leap year start, after Feb 29
    
    duration_days = calculate_duration_days(sample_date1_str, sample_date2_str)
    
    print(f"Duration between {sample_date1_str} and {sample_date2_str}:")
    print(f"{duration_days} days")

    # Another test case: crossing a leap year boundary correctly including Feb 29
    sample_date3_str = "2024-01-01"
    sample_date4_str = "2025-01-01"
    
    duration_days_2 = calculate_duration_days(sample_date3_str, sample_date4_str)
    print(f"\nDuration between {sample_date3_str} and {sample_date4_str}:")
    print(f"{duration_days_2} days (Expected: 365 + 1 leap day adjustment if crossing Feb? Actually exactly 366 days)")

    # Test same year with leap day in middle
    sample_date5_str = "2024-01-01"
    sample_date6_str = "2024-03-01"
    
    duration_days_3 = calculate_duration_days(sample_date5_str, sample_date6_str)
    print(f"\nDuration between {sample_date5_str} and {sample_date6_str}:")
    print(f"{duration_days_3} days (Expected: 28 + 29 + 1 - adjustments? Jan(30)+Feb(29)=59+Mar(1) = 60 days)")