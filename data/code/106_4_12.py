from datetime import date
import calendar

def compute_absolute_year_gap(first_date, second_date):
    year1 = first_date.year
    year2 = second_date.year
    month1 = first_date.month
    day1 = first_date.day
    month2 = second_date.month
    day2 = second_date.day
    
    adjusted_first = date(year1, month1, day1)
    adjusted_second = date(year2, month2, day2)
    
    delta = adjusted_second - adjusted_first
    total_days = abs(delta.days)
    
    is_leap = calendar.isleap(year1) or calendar.isleap(year2)
    days_in_year = 366 if is_leap else 365
    
    years_elapsed = total_days // days_in_year
    
    return years_elapsed

if __name__ == '__main__':
    start = date(2021, 2, 28)
    end = date(2025, 2, 28)
    output = compute_absolute_year_gap(start, end)
    print(output)