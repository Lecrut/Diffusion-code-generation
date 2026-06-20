import datetime

def parse_iso8601_date(iso_string):
    try:
        date_obj = datetime.datetime.fromisoformat(iso_string).date()
        return date_obj
    except ValueError as e:
        print(f"Invalid ISO 8601 date string: {e}")
        return None

def extract_date_components(date_obj):
    if date_obj is not None:
        year = date_obj.year
        month = date_obj.month
        day = date_obj.day
        return year, month, day
    else:
        return None, None, None

if __name__ == '__main__':
    iso_string = "2023-10-15T14:30:00"
    date_obj = parse_iso8601_date(iso_string)
    year, month, day = extract_date_components(date_obj)
    print(f"Year: {year}, Month: {month}, Day: {day}")