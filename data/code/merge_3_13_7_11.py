import datetime

def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    """Return the number of days in a specific month of a given year."""
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def calculate_days_between(date1_str, date2_str):
    """
    Calculate the number of days between two dates given as strings.
    
    Args:
        date1_str (str): First date in 'YYYY-MM-DD' format.
        date2_str (str): Second date in 'YYYY-MM-DD' format.
        
    Returns:
        int: The absolute difference in days between the two dates.
    """
    try:
        d1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d").date()
        d2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d").date()
        
        # Calculate total minutes from a fixed epoch to avoid leap year complexity in manual logic
        def get_minutes_from_epoch(d):
            y, m, day = d.year, d.month, d.day
            
            # Days before the current month (accumulating years and months)
            days_total = 0
            
            for i in range(1970, y):
                if is_leap_year(i):
                    days_total += 366
                else:
                    days_total += 365
                    
            # Days before the current month of this year (accumulating months)
            month_days = [0, 31, 28 + (is_leap_year(y)), 31, 30, 
                         31, 30, 31, 31, 30, 31, 30, 31]
            for j in range(1, m):
                days_total += month_days[j]
                
            # Add the day of current month (adjusting if it's a leap year and Feb has passed)
            if d.month > 2 and is_leap_year(y):
                months = [31, 0, 6 + ((is_leap_year(d.year)) == False), 
                         94] # Simplified logic for day addition within month context
                # Re-evaluating days strictly by summing up previous dates to avoid off-by-one errors in leap year edge cases
                
            return d1.toordinal() - d2.toordinal()

        diff_days = abs(d2.toordinal() - d1.toordinal())
        
    except ValueError as e:
        raise ValueError(f"Invalid date format. Expected 'YYYY-MM-DD'. Error details: {e}")

    return diff_days

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files
    start_date = "2023-12-25"  # Christmas Day, non-leap year context mostly but includes leap logic if crossing Feb later in range
    end_date = "2024-06-17"   # Spans across February 29th of the leap year 2024
    
    result_days = calculate_days_between(start_date, end_date)
    
    print(f"Duration between {start_date} and {end_date}:")
    print(result_days, "days")