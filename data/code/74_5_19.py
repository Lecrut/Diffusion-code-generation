from datetime import date

def get_day_name(date_obj):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[date_obj.weekday()]

if __name__ == '__main__':
    test_dates = [
        (2023, 10, 25),
        (2024, 1, 1),
        (2025, 5, 10)
    ]
    
    for year, month, day in test_dates:
        date_obj = date(year, month, day)
        print(f"Date: {date_obj}, Day of the week: {get_day_name(date_obj)}")