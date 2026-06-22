from datetime import datetime

def parse_date_string(date_str):
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError(f"Invalid date format: {date_str}")
    month_str, day_str, year_str = parts
    if len(month_str) != 2 or len(day_str) != 2 or len(year_str) != 4:
        raise ValueError(f"Invalid date format: {date_str}")
    if not month_str.isdigit() or not day_str.isdigit() or not year_str.isdigit():
        raise ValueError(f"Invalid date format: {date_str}")
    month = int(month_str)
    day = int(day_str)
    year = int(year_str)
    try:
        return datetime(year, month, day)
    except ValueError:
        raise ValueError(f"Invalid date values: {date_str}")

def sort_dates(date_strings):
    if not isinstance(date_strings, list):
        raise ValueError("Input must be a list")
    if len(date_strings) == 0:
        return []
    validated_dates = []
    for ds in date_strings:
        dt_obj = parse_date_string(ds)
        validated_dates.append((dt_obj, ds))
    validated_dates.sort(key=lambda item: item[0])
    return [item[1] for item in validated_dates]

if __name__ == '__main__':
    sample_dates = ['12-31-2023', '01-01-2023', '06-15-2022', '02-28-2023']
    sorted_result = sort_dates(sample_dates)
    print(sorted_result)