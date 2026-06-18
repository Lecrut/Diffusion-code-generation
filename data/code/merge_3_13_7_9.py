import math

def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))

def days_in_month(month, year):
    """Return the number of days in a specific month of a given year."""
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else: # February
        return 29 if is_leap_year(year) else 28

def days_between(date1_str, date2_str):
    """
    Calculate the number of days between two dates given as 'YYYY-MM-DD' strings.
    
    Args:
        date1_str (str): First date in 'YYYY-MM-DD' format.
        date2_str (str): Second date in 'YYYY-MM-DD' format.
        
    Returns:
        int: The absolute number of days between the two dates.
    """
    def parse_date(date_str):
        year, month, day = map(int, date_str.split('-'))
        return year, month, day
    
    y1, m1, d1 = parse_date(date1_str)
    y2, m2, d2 = parse_date(date2_str)
    
    # Convert both dates to absolute days from a reference point (e.g., 0000-03-01 or similar)
    def get_absolute_days(year, month, day):
        total_days = 0
        
        # Add years: Calculate full leap cycles and remaining years
        # A cycle is 400 years with exactly 97 leap years (365*400 + 97)
        
        num_cycles = year // 400
        rem_year_in_cycle = year % 400
        
        total_days += num_cycles * (365 * 400 + 97) # Days in full cycles
        
        current_year = rem_year_in_cycle if rem_year_in_cycle > 0 else 400
        
        while current_year < y1:
            is_l = is_leap_year(current_year)
            total_days += (366 if is_l else 365) + days_before_month(rem_year_in_cycle, m1) # Adjust logic below to be precise
            
            # Let's restructure the year loop for clarity and accuracy without complex math functions that might drift.
            # Simpler approach: Iterate years from a fixed start point up to y1-1
        
        return 0

    def calculate_days_from_epoch(year, month, day):
        """Calculate days since an arbitrary epoch (e.g., year 1)."""
        total = 0
        
        # Days for full centuries and leap cycles before the target year
        num_400_cycles = (year - 1) // 400
        remainder_years_in_cycle = ((year - 1) % 400) + 1
        
        # Add days from complete 400-year cycles: Each has 365*400 + 97 leap years = 146,097 days
        total += num_400_cycles * (365 * 400 + 97)
        
        # Days from the remaining years in the current cycle up to target year - 1
        for y in range(remainder_years_in_cycle):
            is_l = is_leap_year(y) if True else False # We just need logic based on 'y' being part of sequence starting at remainder+1? No.
            
            # Correct iteration: The variable `y` here represents the year index within a 400-year cycle relative to start of that cycle (year 1).
            # Actually, let's iterate from year 1 up to y-1 directly for simplicity if performance allows O(N) or use Zeller-like math. 
            # Given constraints on "efficient", we should avoid pure iteration over centuries if possible, but iterating years is fine unless N is huge.
            # However, to be truly efficient without external libraries like datetime (which handles leap logic internally), let's implement a robust algorithmic approach:
            
            pass

    def get_days_from_year_1(year):
        """Calculate days from year 0 up to the end of 'year'."""
        if year < 400: # Optimization for small cycles? No, keep general.
             total = (365 * year) + math.floor((year - 1)/4)*7 + ... 
        
    # Let's use a standard algorithmic approach often used in competitive programming to avoid O(years) loop if years are large, 
    # though iterating up to year ~2000 is trivial. To be safe and efficient for any integer range:
    
    def count_leaps_before(n):
        """Count number of leap days before year n (i.e., from 1 to n-1)."""
        return math.floor((n - 1) / 4) - math.floor((n - 1) / 100) + math.floor((n - 1) / 400)

    def days_before_month(year, month):
        """Days from start of year to end of previous month."""
        # Days in complete months before 'month'
        d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if is_leap_year(year):
            d[1] = 29
            
        total_days_in_prev_months = sum(d[:month-1])
        return total_days_in_prev_months

    # Calculate absolute days for date1 and date2 relative to year 0 (or a safe epoch)
    
    def get_total_days(y, m, d):
        """Get total number of days from the beginning of time (year 0 approx) until end of day y-m-d."""
        # Days in years before current year
        leaps = count_leaps_before(y + 1) 
        base_years = y - 1 - leaps
        
        # Total days from full previous years
        total_days = base_years * 365 + leaps
        
        # Add days for months and day of current month (assuming non-leap adjustment later if needed, but we handle leap in count_leaps)
        d_in_current_year = sum(days_before_month(y, m)) + d - 1 # -1 because it's inclusive counting from start? 
        # Let's redefine: Day 0 is Jan 1. So day of year index (0-based).

if __name__ == '__main__':
    pass
