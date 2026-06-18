from datetime import date
def format_date_with_month_name(date_obj: date) -> str:
    return f"{date_obj.strftime('%B %d, %Y')}"
if __name__ == '__main__':
    sample_dates = [
        date(2023, 5, 17),
        date.today(),
        date(2099, 12, 31)
    ]
    for d in sample_dates:
        print(format_date_with_month_name(d))