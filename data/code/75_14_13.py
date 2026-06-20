from datetime import date

def is_valid_date(year, month, day):
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

def months_and_years_difference(date1, date2):
    if not (is_valid_date(*date1) and is_valid_date(*date2)):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    years_diff = date2.year - date1.year
    months_diff = date2.month - date1.month
    
    if date2.day < date1.day:
        months_diff -= 1
    
    total_months = (years_diff * 12) + months_diff
    return abs(total_months)

if __name__ == '__main__':
    sample_date1 = (2010, 5, 15)
    sample_date2 = (2023, 8, 20)
    print(months_and_years_difference(sample_date1, sample_date2))