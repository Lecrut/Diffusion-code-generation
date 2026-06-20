from datetime import date

def is_valid_date(year, month, day):
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

def get_day_name(date_obj):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[date_obj.weekday()]

if __name__ == '__main__':
    date1 = (2023, 10, 25)
    if is_valid_date(*date1):
        print(f"Date: {date(date1)}, Day of the week: {get_day_name(date(*date1))}")
    
    date2 = (2024, 1, 1)
    if is_valid_date(*date2):
        print(f"Date: {date(date2)}, Day of the week: {get_day_name(date(*date2))}")
    
    date3 = (2025, 12, 25)
    if is_valid_date(*date3):
        print(f"Date: {date(date3)}, Day of the week: {get_day_name(date(*date3))}")
    
    date4 = (2026, 7, 4)
    if is_valid_date(*date4):
        print(f"Date: {date(date4)}, Day of the week: {get_day_name(date(*date4))}")