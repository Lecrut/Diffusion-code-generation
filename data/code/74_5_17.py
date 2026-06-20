from datetime import date

DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_day_name(date_obj):
    return DAYS_OF_WEEK[date_obj.weekday()]

if __name__ == '__main__':
    sample_dates = [
        date(2023, 10, 25),
        date(2024, 1, 1),
        date(2025, 12, 31)
    ]
    
    for sample_date in sample_dates:
        print(f"Date: {sample_date}, Day of the week: {get_day_name(sample_date)}")