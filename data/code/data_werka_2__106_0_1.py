from datetime import datetime

def calculate_year_difference(date1: str, date2: str) -> int:
    fmt = "%Y-%m-%d"
    dt1 = datetime.strptime(date1, fmt)
    dt2 = datetime.strptime(date2, fmt)
    return abs(dt1.year - dt2.year)

if __name__ == '__main__':
    result = calculate_year_difference("2023-10-01", "2020-10-01")
    print(result)