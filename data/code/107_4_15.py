from datetime import datetime

def format_date(date_str: str) -> str:
    parts = date_str.split(".")
    day = int(parts[0])
    month = int(parts[1])
    year = int(parts[2])
    date_obj = datetime(year=year, month=month, day=day)
    return date_obj.strftime("%Y-%m-%d")

if __name__ == '__main__':
    print(format_date("14.02.1989"))
    print(format_date("20.10.2023"))
    print(format_date("30.06.1970"))