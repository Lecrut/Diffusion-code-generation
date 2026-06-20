import datetime

def parse_iso_date(iso_string):
    try:
        return datetime.datetime.fromisoformat(iso_string).date()
    except ValueError as e:
        raise ValueError(f"Invalid ISO date format: {iso_string}") from e

if __name__ == '__main__':
    iso_date = "2023-10-15T14:30:00"
    date_obj = parse_iso_date(iso_date)
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    print(f"Year: {year}, Month: {month}, Day: {day}")