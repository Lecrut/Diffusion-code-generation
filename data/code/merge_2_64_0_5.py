import datetime
from dateutil import parser as dt_parser
def format_date_with_full_month(date_obj):
    if isinstance(date_obj, str):
        parsed = dt_parser.parse(date_obj)
        return parsed.strftime("%B %Y")
    if not hasattr(date_obj, 'astimezone'):
        raise ValueError("Input must be a datetime object or string.")
    normalized = date_obj.astimezone(datetime.timezone.utc)
    return f"{normalized.strftime('%B')} {normalized.year}"
if __name__ == '__main__':
    sample_dates = [
        "2023-10-05 14:30",
        datetime.datetime(2024, 6, 18),
        "Dec 25, 2023"
    ]
    for d in sample_dates:
        try:
            result = format_date_with_full_month(d)
            print(result)
        except Exception as e:
            print(f"Error processing {d}: {e}")