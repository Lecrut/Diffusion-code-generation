from datetime import datetime

def year_difference(date_str1: str, date_str2: str) -> int:
    fmt = "%Y-%m-%d"
    d1 = datetime.strptime(date_str1, fmt)
    d2 = datetime.strptime(date_str2, fmt)
    return abs(d1.year - d2.year)

if __name__ == '__main__':
    result = year_difference("2020-02-29", "2023-03-01")
    print(result)