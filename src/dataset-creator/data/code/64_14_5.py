import datetime
def format_date_with_month_name(date_obj: datetime.date) -> str:
    return f"{date_obj.strftime('%B %d, %Y')}"
if __name__ == '__main__':
    sample_dates = [
        datetime.date(2023, 10, 5),
        datetime.date(2024, 6, 15),
        datetime.datetime.now().date()
    ]
    for date in sample_dates:
        print(format_date_with_month_name(date))