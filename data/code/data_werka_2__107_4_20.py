from datetime import datetime

def transform_date(date_str: str) -> str:
    parts = date_str.split('.')
    if len(parts) != 3:
        raise ValueError("Invalid date format")
    day, month, year = parts
    try:
        dt = datetime(int(year), int(month), int(day))
    except ValueError:
        raise ValueError("Invalid date values")
    return dt.strftime("%Y-%m-%d")

if __name__ == '__main__':
    print(transform_date("25.12.2023"))
    print(transform_date("01.01.2000"))
    print(transform_date("31.12.1999"))
    print(transform_date("15.08.2021"))