import datetime

def parse_and_extract_date_components(iso_date_str):
    try:
        date_obj = datetime.datetime.fromisoformat(iso_date_str)
        year = date_obj.year
        month = date_obj.month
        day = date_obj.day
        return year, month, day
    except ValueError as e:
        raise ValueError("Invalid ISO 8601 date string") from e

if __name__ == '__main__':
    sample_date = "2023-10-15T14:30:00"
    try:
        year, month, day = parse_and_extract_date_components(sample_date)
        print(f"Year: {year}, Month: {month}, Day: {day}")
    except ValueError as e:
        print(e)