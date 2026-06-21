from datetime import datetime

def year_difference(date1_str: str, date2_str: str) -> int:
    fmt = "%Y-%m-%d"
    d1 = datetime.strptime(date1_str, fmt)
    d2 = datetime.strptime(date2_str, fmt)
    diff = d2 - d1
    days = diff.days
    years = days // 365
    return years

if __name__ == '__main__':
    result = year_difference("2020-01-01", "2023-06-15")
    print(result)