from datetime import date
def format_date_with_month_name(date_obj):
    return f"{date_obj.strftime('%B')} {date_obj.day}" if isinstance(date_obj, date) else "Invalid Date Object"
if __name__ == '__main__':
    sample_dates = [
        date(2023, 10, 5),
        date(2024, 6, 15),
        date(2025, 12, 31)
    ]
    for d in sample_dates:
        print(format_date_with_month_name(d))