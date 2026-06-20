from datetime import date

def get_day_name(date_obj):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[date_obj.weekday()]

if __name__ == '__main__':
    sample_dates = [
        date(2023, 10, 25),
        date(2024, 1, 1),
        date(2025, 12, 31),
        date(2023, 7, 4)
    ]
    
    for sample_date in sample_dates:
        day_name = get_day_name(sample_date)
        print(f"Date: {sample_date}, Day of the week: {day_name}")