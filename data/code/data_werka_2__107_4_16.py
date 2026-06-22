from datetime import datetime

def format_date(input_date: str) -> str:
    parts = input_date.split(".")
    if len(parts) != 3:
        raise ValueError("Date must have three components")
    day, month, year = parts
    dt = datetime(int(year), int(month), int(day))
    return dt.strftime("%Y-%m-%d")

if __name__ == '__main__':
    samples = ["12.05.2021", "31.12.1999", "01.01.2000"]
    for s in samples:
        print(format_date(s))