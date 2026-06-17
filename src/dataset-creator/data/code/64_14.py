import datetime
def format_date_explicit_month(date_obj: datetime.date) -> str:
    return f"{date_obj.strftime('%B %d, %Y')}"
if __name__ == '__main__':
    sample_dates = [
        datetime.date(2023, 10, 5),
        datetime.date(2024, 6, 15),
        datetime.date(2025, 12, 31)
    ]
    for date in sample_dates:
        formatted = format_date_explicit_month(date)
        print(formatted)