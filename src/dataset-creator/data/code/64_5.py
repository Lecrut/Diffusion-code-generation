from datetime import date
def format_date_with_month_name(date_obj: date) -> str:
    return f"{date_obj.strftime('%B %d, %Y')}"
if __name__ == '__main__':
    sample_dates = [
        date(2023, 5, 17),
        date(2024, 12, 25),
        date(2020, 8, 9)
    ]
    for d in sample_dates:
        print(format_date_with_month_name(d))