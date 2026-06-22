from datetime import datetime

MONTH_NAMES = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
    "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
}

def format_date(date_str: str) -> str:
    parts = date_str.split(".")
    day = int(parts[0])
    month_str = parts[1]
    year = int(parts[2])
    
    if month_str in MONTH_NAMES:
        month = MONTH_NAMES[month_str]
    else:
        month = int(month_str)
        
    dt = datetime(year=year, month=month, day=day)
    return dt.strftime("%Y-%m-%d")

if __name__ == '__main__':
    samples = ["25.12.2023", "01.01.2000", "31.12.1999"]
    for s in samples:
        print(format_date(s))