from datetime import date
def format_date_explicit_month(date_obj: date) -> str:
    return f"{date_obj.strftime('%B %d, %Y')}"
if __name__ == '__main__':
    sample_dates = [
        date(2023, 5, 17),
        date(2024, 12, 31),
        date(2025, 6, 1)
    ]
    for d in sample_dates:
        print(format_date_explicit_month(d))