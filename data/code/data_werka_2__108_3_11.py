def extract_day(date_str):
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    parts = date_str.split("-")
    if len(parts) != 3:
        raise ValueError("Date string must have three parts")
    year, month, day = parts
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        raise ValueError("Date components must have correct lengths")
    return day

if __name__ == '__main__':
    sample_date = "2024-12-25"
    day_value = extract_day(sample_date)
    print(day_value)