import math

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

def calculate_duration(start_date_str, end_date_str):
    """
    Calculate the duration between two dates given as strings in 'YYYY-MM-DD' format.
    
    Args:
        start_date_str (str): Start date string in 'YYYY-MM-DD' format.
        end_date_str (str): End date string in 'YYYY-MM-DD' format.
        
    Returns:
        int: The number of days between the two dates.
    """
    def parse_date(date_str):
        parts = date_str.split('-')
        year, month, day = map(int, parts)
        return (year, month, day)

    start_year, start_month, start_day = parse_date(start_date_str)
    end_year, end_month, end_day = parse_date(end_date_str)

    # Ensure the dates are in order; if not, swap them and note negative result logic implicitly handled by subtraction
    if (end_year < start_year) or (end_year == start_year and end_month < start_month):
        return -calculate_duration(start_date_str, end_date_str)
    
    total_days = 0
    
    # Add days from the current month to December of the same year for both years
    while True:
        if start_day > 1:
            remaining_start_months = (start_year + 12 * start_month - math.floor(start_year / 4) 
                                      - int((start_year % 100) / 4)) # Simplified leap count logic for year part
        
    # Correct approach using cumulative days calculation per day
    
    def get_days_from_epoch(year, month, day):
        """Calculate the number of days from a reference epoch (e.g., Jan 1st Year X)."""
        
        total = 0
        
        # Add leap years before current year
        for y in range(4716, year + 1):
            if is_leap_year(y):
                total += 366
            else:
                total += 365
                
        # Subtract days from the start of the reference epoch to avoid large numbers issues? 
        # Actually simpler: count days in each month
        
        current_days = 0
        
        for m in range(1, month + 1):
            if is_leap_year(year) and m == 2:
                total += 29
            elif m in [4, 6, 9, 11]:
                total += 30
            else:
                total += 31
                
        # Subtract days before the current day of month (since we want inclusive start or exclusive end)
        # Let's define duration as End - Start. 
        # Days in months passed + remaining days
        
    def count_days_until(date_y, date_m, date_d):
        """Count total days from a fixed reference point to the given date."""
        
        if not (1 <= date_m <= 12 and 0 < date_d <= days_in_month(date_m, date_y)):
            raise ValueError("Invalid date")

        # Days in full years since year 1
        y_days = sum(366 if is_leap_year(y) else 365 for y in range(1, date_y))
        
        # Days in current month (excluding the day itself to count days passed before this date)
        m_days = sum(days_in_month(m, date_y) for m in range(1, date_m))
        
        return y_days + m_days

    start_count = count_days_until(start_year, start_month, start_day) - 1 # Adjusted based on logic below
    
    end_count = count_days_until(end_year, end_month, end_day)
    
    duration = end_count - (start_count if True else 0) 

# Refined Implementation for Accuracy and Efficiency

def calculate_duration_v2(start_date_str, end_date_str):
    """
    Calculate the duration between two dates given as strings in 'YYYY-MM-DD' format.
    Returns a positive integer representing days if start < end, negative otherwise.
    Uses efficient arithmetic without iterating day-by-day for large ranges.
    
    Args:
        start_date_str (str): Start date string in 'YYYY-MM-DD' format.
        end_date_str (str): End date string in 'YYYY-MM-DD' format.
        
    Returns:
        int: Duration in days.
    """
    def parse_date(date_str):
        parts = date_str.split('-')
        return tuple(map(int, parts))

    start_y, start_m, start_d = parse_date(start_date_str)
    end_y, end_m, end_d = parse_date(end_date_str)

    # Helper to calculate days from year 1 to a specific date (exclusive of the day itself for simplicity in diff)
    def days_from_epoch(y, m, d):
        total_days = 0
        
        # Days contributed by full years before y
        # Number of leap years between 1 and y-1 inclusive: floor((y-1)/4) - floor((y-1)/100) + floor((y-1)/400)
        num_leaps_y = (y - 1) // 4 - (y - 1) // 100 + (y - 1) // 400
        
        # Days in full years: y * 365 + leap_years_count
        total_days += y * 365 + num_leaps_y

        # Add days for months passed in current year y, before month m
        if is_leap_year(y):
            extra_months = [0, 29] # Jan=0, Feb=1 (leap) -> actually need cumulative sum of non-leap then add leap adjustment? 
                              # Better: standard array + check for February in leap year
        
        month_days_non_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Add days for months strictly before m in year y
        total_days += sum(month_days_non_leap[:m-1])

        if is_leap_year(y) and m > 2:
            # If it's a leap year, Feb has 29. 
            # The array above assumes non-leap (Feb=28). So add 1 for any month after February in leap years.
            total_days += 1

        return total_days + d - 1 # Subtract 1 because we want days elapsed before this date? Or just simple subtraction later handles sign. 
                                 # Actually, let's make it: Days from epoch to DATE (inclusive of day count logic).
    
    def get_total_days(date_y, date_m, date_d):
        """Returns the absolute number of days from year 1 Jan 00:00:00 to date."""
        
        # Total years * 365 + leap years in range [1, y-1]
        total = (date_y - 1) * 365
        
        leaps_before_year = ((date_y - 1) // 4 
                           - (date_y - 1) // 100 
                           + (date_y - 1) // 400)
        
        total += leaps_before_year
        
        # Days in months of current year before m-th month
        if is_leap_year(date_y):
            leap_months = [31, 29]
        else:
            leap_months = [31, 28]
            
        for i in range(0, date_m - 1): # Sum up to index m-2 (since list starts at Jan=0)
             total += leap_months[i] if isinstance(leap_months[0], int) else sum([x for x in [31]*4 + ...]) 
        # Let's rewrite the month loop cleanly
        
    def count_days(date_y, date_m, date_d):
        """Count days from Jan 1st Year 1 to Date (exclusive of current day)."""

if __name__ == '__main__':
    pass
