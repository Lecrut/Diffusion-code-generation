from datetime import date
def format_date_explicit_month(date_obj: date) -> str:
    return f"{date_obj.day}, {date_obj.strftime('%B %Y')}"
if __name__ == '__main__':
    sample_dates = [
        date(2023, 10, 5),
        date(2024, 7, 18),
        date(2025, 12, 31)
    ]
    for d in sample_dates:
        print(format_date_explicit_month(d))