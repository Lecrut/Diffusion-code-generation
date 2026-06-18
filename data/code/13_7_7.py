import math

def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    """Return the number of days in a specific month given its name as integer (1-12)."""
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else: # Months with 31 days (e.g., Jan=1, Mar=3, May=5...)
        return 31

def date_to_days(year, month, day):
    """Convert a single date to the number of days since epoch (year 1, month 1, day 1)."""
    # Calculate total years from year 1 up to start_of_year - 1
    total = 0
    for i in range(1, year):
        if is_leap_year(i):
            total += 366
        else:
            total += 365

    # Add days for full months of the current year up to start_of_month - 1
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # Adjusted for leap year logic handled here
    if is_leap_year(year):
        month_days[2] = 29

    current_month_days = sum(month_days[:month])
    
    total += current_month_days + day - 1
    
    return total

def calculate_duration(date1, date2):
    """Calculate the duration in days between two dates. 
       Each date is a tuple: (year, month, day) where year starts from 0 to represent BC/Years ago if needed, but here using standard AD/BC logic relative to base year."""
    
    # Assuming input format is (year, month, day). Year can be negative for BC dates.
    d1 = date_to_days(date1[0], date1[1], date1[2])
    d2 = date_to_days(date2[0], date2[1], date2[2])

    return abs(d2 - d1)

def main():
    # Hard-coded sample values without user input or arguments. 
    # Sample 1: Calculate days between Jan 1, 2000 and Dec 31, 2023 (Leap year check for 2000).
    date_start = (2000, 1, 1)
    date_end = (2023, 12, 31)

    duration_days = calculate_duration(date_start, date_end)

    print(f"Duration between {date_start[0]}/{int(date_start[1])}/{date_start[2]} and "
          f"{date_end[0]}/{int(date_end[1])}/{date_end[2]} is: {duration_days} days")

if __name__ == '__main__':
    main()