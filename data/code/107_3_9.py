import email.utils
import datetime

def format_rfc2822(dt: datetime.datetime) -> str:
    return email.utils.format_datetime(dt, usegmt=True)

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 25, 14, 30, 0, tzinfo=datetime.timezone.utc)
    print(format_rfc2822(sample_date))
    
    sample_date_naive = datetime.datetime(2024, 1, 1, 12, 0, 0)
    print(format_rfc2822(sample_date_naive))