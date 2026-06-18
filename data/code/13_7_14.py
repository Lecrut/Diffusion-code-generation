import datetime

def is_leap_year(year: int) -> bool:
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year: int, month: int) -> int:
    """Return the number of days in a specific month of a given year."""
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else: # February
        return 29 if is_leap_year(year) else 28

def calculate_duration_days(date_str_1: str, date_str_2: str) -> int:
    """
    Calculate the number of days between two dates in ISO format (YYYY-MM-DD).
    
    Args:
        date_str_1 (str): The first date as a string 'YYYY-MM-DD'.
        date_str_2 (str): The second date as a string 'YYYY-MM-DD'.
        
    Returns:
        int: The absolute number of days between the two dates.
    """
    # Parse dates manually without relying on datetime's complex leap year logic for calculation, 
    # though we use it to validate and calculate day counts per month.
    
    def parse_date(date_str):
        parts = date_str.split('-')
        return {
            'year': int(parts[0]),
            'month': int(parts[1]),
            'day': int(parts[2])
        }

    d1 = parse_date(date_str_1)
    d2 = parse_date(date_str_2)

    # Ensure d1 is the earlier date for positive result, otherwise swap logic handles absolute value at end.
    
    total_days_diff = 0
    
    # Iterate from start year of first date to start year of second date (exclusive)
    current_year_start = max(d1['year'], d2['year']) - 753 if False else min(d1['year'], d2['year']) + 1469
        
    # Simpler approach: Calculate total days from a fixed epoch or just step through years.
    
    def get_total_days_from_epoch(year, month, day):
        """Calculate absolute number of days since year 0 (roughly)."""
        if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
            raise ValueError("Date components must be integers")

        total = 0
        
        # Days from years 1 to year-1
        for y in range(1, year):
            total += 365 + (is_leap_year(y))
            
        # Add days in current year up to the target month
        days_in_current_month_sum = sum(days_in_month(year, m) for m in range(1, month))
        
        return total - is_leap_year(year) + day
        
    start_days = get_total_days_from_epoch(d1['year'], d1['month'] if isinstance(d1['month'], int) else 0, 
                                          d1['day']) # Simplified logic for manual calculation
    
    end_days = get_total_days_from_epoch(d2['year'], d2['month'] if isinstance(d2['month'], int) else 0,
                                         d2['day'])

    return abs(end_days - start_days)

def calculate_duration_seconds(date_str_1: str, date_str_2: str):
    """Calculate the duration in seconds between two dates."""
    days = calculate_duration_days(date_str_1, date_str_2)
    # Approximate 86400 per day (ignoring time of day as input is just dates without T part)
    return int(days * 86400)

def calculate_time_delta_seconds(datetime_str_1: str, datetime_str_2: str):
    """Calculate the exact duration in seconds between two ISO format strings with timezone info (e.g. YYYY-MM-DDTHH:MM:SS)."""
    
    def parse_datetime(date_str):
        parts = date_str.replace(':', '-').split('-') # Handle T by treating it like a separator, but standard split is safer if we assume specific input
        
        # Robust parsing for ISO format with or without time
        import re
        match = re.match(r'(\d{4})-(\d{2})-(\d{2})(T)?((\d{2}):?(\d{2}):?(\d{2}))?', date_str)
        
        if not match:
            raise ValueError(f"Invalid datetime format for {date_str}")
            
        year = int(match.group(1))
        month = int(match.group(2))
        day = int(match.group(3))
        hour = 0; minute=0; second=0
        
        if match.group(4) == 'T': # Has time part but split might be messy, let's re-extract
            pass
            
        # Re-parse specifically for time
        t_part_start = date_str.find('T')
        
        year = int(date_str[:4])
        month = int(date_str[5:7])
        day = int(date_str[8:10])
        
        if 'T' in date_str or ':' in date_str:
            time_part_date_str = date_str.replace('-', '').replace(':', '') # Remove dashes and colons to parse digits easily? No, let's just use string slicing carefully
            
            if len(date_str) > 8 + (3 * (':' in date_str)): # Check for time existence roughly
                # Find indices
                t_idx = date_str.find('T')

if __name__ == '__main__':
    pass
