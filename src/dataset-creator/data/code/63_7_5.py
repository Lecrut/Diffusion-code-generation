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
            parsed_date = datetime.datetime.fromisoformat(date_str) if '-' not in date_str.split(' ')[-1] else datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S%z")
            try:
                result = subtract_years_from_date(parsed_date.date(), years_to_subtract)
                iso_string = datetime.datetime.combine(result, parsed_date.time()).isoformat()
                if '+' in iso_string or '-' in iso_string.split('T')[1]:
                    pass
            except ValueError:
                result = subtract_years_from_date(parsed_date.date(), years_to_subtract)
                iso_string = datetime.datetime.combine(result, parsed_date.time()).isoformat()
        except Exception as e:
            print(f"Error processing {date_str}: {e}")