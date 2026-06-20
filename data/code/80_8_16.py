from datetime import datetime

def parse_date(date_str: str) -> datetime:
    return datetime.strptime(date_str, "%Y-%m-%d")

def compare_dates(date1: datetime, date2: datetime) -> int:
    if date1 < date2:
        return -1
    elif date1 > date2:
        return 1
    else:
        return 0

def format_date(date_obj: datetime) -> str:
    return date_obj.strftime("%Y-%m-%d")

if __name__ == '__main__':
    date_str1 = "2023-04-01"
    date_str2 = "2023-05-01"

    date1 = parse_date(date_str1)
    date2 = parse_date(date_str2)

    print("Date 1:", format_date(date1))
    print("Date 2:", format_date(date2))

    comparison_result = compare_dates(date1, date2)
    if comparison_result == -1:
        print(f"{date_str1} is earlier than {date_str2}")
    elif comparison_result == 1:
        print(f"{date_str1} is later than {date_str2}")
    else:
        print(f"{date_str1} and {date_str2} are the same")