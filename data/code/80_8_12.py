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

    comparison_result = compare_dates(date1, date2)
    formatted_date = format_date(date1)

    print("Comparison Result:", comparison_result)
    print("Formatted Date:", formatted_date)