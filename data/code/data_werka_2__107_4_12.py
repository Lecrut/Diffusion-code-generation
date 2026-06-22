import datetime

def format_date(date_str: str) -> str:
    parts = date_str.split(".")
    if len(parts) != 3:
        raise ValueError("Invalid format")
    day, month, year = parts
    dt = datetime.datetime(int(year), int(month), int(day))
    return dt.strftime("%Y-%m-%d")

if __name__ == '__main__':
    print(format_date("05.06.2021"))
    print(format_date("31.12.2000"))
    print(format_date("01.01.2024"))