import email.utils
import datetime

def format_rfc2822(dt: datetime.datetime) -> str:
    return email.utils.format_datetime(dt, usegmt=True)

if __name__ == '__main__':
    sample_dates = [
        datetime.datetime(2023, 10, 5, 14, 30, 0),
        datetime.datetime(2024, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc),
        datetime.datetime(1999, 12, 31, 23, 59, 59),
    ]
    for dt in sample_dates:
        print(format_rfc2822(dt))