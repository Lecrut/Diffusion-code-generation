def get_day(date_str: str) -> str:
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    if len(date_str) != 10:
        raise ValueError("Date string must be 10 characters long")
    if date_str[4] != '-' or date_str[7] != '-':
        raise ValueError("Date string must use hyphens as separators")
    year_part = date_str[0:4]
    month_part = date_str[5:7]
    day_part = date_str[8:10]
    if not year_part.isdigit() or not month_part.isdigit() or not day_part.isdigit():
        raise ValueError("Date components must be digits")
    return day_part

if __name__ == '__main__':
    sample_date = "2024-02-14"
    result = get_day(sample_date)
    print(result)