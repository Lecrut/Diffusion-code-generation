import datetime
from dateutil.relativedelta import relativedelta
def subtract_years_from_date(date_obj: datetime.date, years_to_subtract: int) -> datetime.date:
    return date_obj - relativedelta(years=years_to_subtract)
if __name__ == '__main__':
    sample_dates = [
        "2023-10-05",
        "2024-06-15T14:30:00+02:00"
    ]
    years_to_subtract = 5
    for date_str in sample_dates:
        try:
            parsed_date = datetime.datetime.fromisoformat(date_str) if ':' in date_str else datetime.date.fromisoformat(date_str)
            new_date = subtract_years_from_date(parsed_date, years_to_subtract)
            iso_string = new_date.isoformat()
            print(f"Original Date (ISO 8601): {date_str}")
            print(f"Subtracted Years: {years_to_subtract}")
            print(f"Resulting Date (ISO 8601): {iso_string}\n")
        except ValueError as e:
            print(f"Error parsing date '{date_str}': {e}")