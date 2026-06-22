from dateutil.parser import parse as _parse_date

def get_day_of_week(date_string: str) -> str:
    if not isinstance(date_string, str):
        raise ValueError("Input must be a string")
    if not date_string.strip():
        raise ValueError("Input string cannot be empty")
    try:
        date_obj = _parse_date(date_string)
    except Exception as exc:
        raise ValueError(f"Unable to parse date: {date_string}") from exc
    return date_obj.strftime('%A')

if __name__ == '__main__':
    sample_date = 'January 15, 2023'
    result = get_day_of_week(sample_date)
    print(result)