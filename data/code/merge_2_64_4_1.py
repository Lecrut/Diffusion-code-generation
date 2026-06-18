import datetime as dt
def format_datetime_to_text(d: dt.datetime) -> str:
    return f"{d.strftime('%A, %B %d, %Y at %I:%M%p')}"
if __name__ == '__main__':
    sample_date = dt.datetime(2023, 10, 5, 14, 30)
    print(format_datetime_to_text(sample_date))