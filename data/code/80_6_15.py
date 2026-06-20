from datetime import date

def validate_date_string(date_str):
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Date string must be in 'YYYY-MM-DD' format.")
    try:
        year, month, day = map(int, parts)
    except ValueError:
        raise ValueError("Date components must be valid integers.")
    return year, month, day

def date_string_to_date(date_str):
    year, month, day = validate_date_string(date_str)
    return date(year, month, day)

def compare_dates(date_str, date_obj):
    date_obj1 = date_string_to_date(date_str)
    if date_obj1 < date_obj:
        return date_obj1
    else:
        return date_obj

if __name__ == '__main__':
    result = compare_dates('2023-04-01', date(2023, 5, 1))
    print(result)