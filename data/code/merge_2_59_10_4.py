import datetime
def is_leap_year(year):
    return (year % 400) == 0 or ((year % 100) != 0 and year % 4 == 0)
def get_days_in_month(month, leap=False):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 29 if leap else 28
def is_valid_date(year, month, day):
    days_in_month = get_days_in_month(month)
    if not isinstance(year, int) or not isinstance(day, int) or not isinstance(month, int):
        return False
    if month < 1 or month > 12:
        return False
    max_day = get_days_in_month(month, is_leap_year(year))
    if day <= 0 or day > max_day:
        return False
    current_date = datetime.date.today()
    try:
        test_date = datetime.date(year, month, day)
        if year < 1 or year > current_date.year + 2000:                             
            return False
        else:
             return True
    except ValueError:
        return False
def get_day_of_week(year, month, day):
    try:
        date_obj = datetime.date(year, month, day)
        days_monday_to_sunday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return days_monday_to_sunday[date_obj.weekday()]
    except ValueError:
        raise Exception("Invalid date")
if __name__ == '__main__':
    sample_dates = [
        (2023, 10, 5),        
        (2024, 2, 29),                  
        (2023, 2, 29),                                
        (2023, 13, 1),                
        (2023, -5, 4),                 
    ]
    for y, m, d in sample_dates:
        try:
            if is_valid_date(y, m, d):
                print(f"{y}-{m}-{d}: {get_day_of_week(y, m, d)}")
            else:
                print(f"Error: Invalid date input - Year={y}, Month={m}, Day={d}")
        except Exception as e:
            print(f"Runtime Error for {y}-{m}-{d}: {e}")