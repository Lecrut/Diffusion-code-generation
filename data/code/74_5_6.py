from datetime import date

def get_day_name(date_obj):
    if not isinstance(date_obj, date):
        raise ValueError("Input must be a date object")
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[date_obj.weekday()]

if __name__ == '__main__':
    date1 = date(2023, 10, 25)
    print(f"Date: {date1}, Day of the week: {get_day_name(date1)}")
    
    date2 = date(2024, 1, 1)
    print(f"Date: {date2}, Day of the week: {get_day_name(date2)}")
    
    date3 = date(2025, 12, 25)
    print(f"Date: {date3}, Day of the week: {get_day_name(date3)}")
    
    date4 = date(2026, 7, 4)
    print(f"Date: {date4}, Day of the week: {get_day_name(date4)}")

    try:
        invalid_date = "not a date"
        get_day_name(invalid_date)
    except ValueError as e:
        print(e)