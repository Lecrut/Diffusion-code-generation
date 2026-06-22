from datetime import datetime

def validate_date_string(date_str):
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    parts = date_str.split('/')
    if len(parts) != 3:
        raise ValueError("Date must have exactly 3 parts separated by slashes")
    day_str, month_str, year_str = parts
    if not (day_str.isdigit() and month_str.isdigit() and year_str.isdigit()):
        raise ValueError("Date parts must be numeric")
    day = int(day_str)
    month = int(month_str)
    year = int(year_str)
    if not (1 <= day <= 31):
        raise ValueError("Day out of range")
    if not (1 <= month <= 12):
        raise ValueError("Month out of range")
    if year < 1:
        raise ValueError("Year out of range")
    try:
        datetime(year=year, month=month, day=day)
    except ValueError as e:
        raise ValueError(f"Invalid date: {date_str}") from e
    return date_str

def sort_dates_chronologically(date_strings):
    validated = [validate_date_string(ds) for ds in date_strings]
    return sorted(validated, key=lambda ds: datetime.strptime(ds, '%d/%m/%Y'))

if __name__ == '__main__':
    sample_dates = ['01/01/2024', '15/06/2023', '31/12/2022', '25/12/2023']
    sorted_dates = sort_dates_chronologically(sample_dates)
    print(sorted_dates)