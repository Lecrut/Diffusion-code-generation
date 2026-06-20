import datetime

def parse_iso8601_to_datetime(iso_string):
    try:
        return datetime.datetime.fromisoformat(iso_string)
    except ValueError as e:
        print(f"Error parsing ISO 8601 date: {e}")
        return None

def extract_date_components(date_obj):
    if date_obj is not None:
        return date_obj.year, date_obj.month, date_obj.day
    else:
        return None, None, None

if __name__ == '__main__':
    iso_string = "2023-10-15T12:34:56.789Z"
    parsed_date = parse_iso8601_to_datetime(iso_string)
    year, month, day = extract_date_components(parsed_date)
    print(f"Year: {year}, Month: {month}, Day: {day}")